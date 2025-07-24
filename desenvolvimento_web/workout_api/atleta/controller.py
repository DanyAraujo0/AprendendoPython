from datetime import datetime
from sqlite3 import IntegrityError
from uuid import uuid4
from fastapi import APIRouter, Body, Depends, status, HTTPException, Query
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate as paginate_sqlalchemy
from pydantic import UUID4
from workout_api.centro_treinamento.models import CentroTreinamentoModel
from workout_api.categorias.models import CategoriaModel
from workout_api.atleta.models import AtletaModel
from workout_api.atleta.schemas import AtletaIn, AtletaOut, AtletaUpdate
from workout_api.contrib.dependencies import DatabaseDependency
from sqlalchemy.future import select

router = APIRouter()

async def atleta_by_id(
    id: UUID4, 
    db_session: DatabaseDependency
    ) -> AtletaModel:
    atleta = (
        await db_session.execute(select(AtletaModel).filter_by(id=id))
    ).scalars().first()

    if not atleta:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Atleta não encontrado no id: {id}',
        )
    return atleta

async def get_categoria_e_ct(
        db_session: DatabaseDependency,
        atleta_in: AtletaIn = Body(...),
    ) -> tuple[CategoriaModel, CentroTreinamentoModel]:

    categoria_name = atleta_in.categoria.nome
    centro_treinamento_name = atleta_in.centro_treinamento.nome
    
    categoria = (await db_session.execute(
        select(CategoriaModel).filter_by(nome=categoria_name))
    ).scalars().first()

    if not categoria:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'Categoria "{categoria_name}" não encontrada.'
        )

    centro_treinamento = (await db_session.execute(
        select(CentroTreinamentoModel).filter_by(nome=centro_treinamento_name))
    ).scalars().first()

    if not centro_treinamento:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'Centro de treinamento "{centro_treinamento_name}" não encontrado.'
        )
        
    return categoria, centro_treinamento

@router.post(
    '/',
    summary='Criar novo atleta',
    status_code=status.HTTP_201_CREATED,
    response_model=AtletaOut,
)
async def create(
    db_session: DatabaseDependency,
    dados_validados: tuple = Depends(get_categoria_e_ct),
    atleta_in: AtletaIn = Body(...) 
):
    categoria, centro_treinamento = dados_validados
    
    try:
        atleta_out = AtletaOut(id=uuid4(), created_at=datetime.utcnow(), **atleta_in.model_dump())
        atleta_model = AtletaModel(**atleta_out.model_dump(exclude={'categoria', 'centro_treinamento'}))
        
        atleta_model.categoria_id = categoria.pk_id
        atleta_model.centro_treinamento_id = centro_treinamento.pk_id

        db_session.add(atleta_model)
        await db_session.commit()

    except IntegrityError: # arrumar
        raise HTTPException(
            status_code=status.HTTP_303_SEE_OTHER,
            detail=f"Já existe um atleta cadastrado com o cpf: {atleta_in.cpf}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f'Ocorreu um erro ao inserir os dados no banco: {e}'
        )

    return atleta_out

# @router.get(
#     '/',
#     summary='Consultar todos os Atletas',
#     status_code=status.HTTP_200_OK,
#     response_model=list[AtletaOut],
# )
# async def get_all(db_session: DatabaseDependency) -> list[AtletaOut]:
#     atletas = (await db_session.execute(select(AtletaModel))).scalars().all()
#     return atletas

@router.get(
    '/{id}',
    summary='Consultar um Atleta pelo id',
    status_code=status.HTTP_200_OK,
    response_model=AtletaOut,
)
async def get_by_id(atleta: AtletaModel = Depends(atleta_by_id)) -> AtletaOut:
    return atleta

@router.patch(
    '/{id}',
    summary='Editar um Atleta pelo id',
    status_code=status.HTTP_200_OK,
    response_model=AtletaOut,
)
async def update(
    db_session: DatabaseDependency,
    atleta: AtletaModel = Depends(atleta_by_id),
    atleta_up: AtletaUpdate = Body(...)
) -> AtletaOut:
   
    atleta_update_data = atleta_up.model_dump(exclude_unset=True)
    
    for key, value in atleta_update_data.items():
        setattr(atleta, key, value)
    
    await db_session.commit()
    await db_session.refresh(atleta)
    
    return atleta

@router.delete(
    '/{id}',
    summary='Deletar um Atleta pelo id',
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_by_id(
    db_session: DatabaseDependency,
    atleta: AtletaModel = Depends(atleta_by_id)
) -> None: 
 
    await db_session.delete(atleta)
    await db_session.commit()

@router.get(
    '/',
    summary='Consultar todos os Atletas ou pelo Nome/CPF',
    status_code=status.HTTP_200_OK,
    response_model= Page[AtletaOut],
)
async def get_all(
    db_session: DatabaseDependency,
    nome:  str = Query(None, description="Filtrar atletas pelo nome"), 
    cpf:  str = Query(None, description="Filtrar atletas pelo cpf"),
    )->Page[AtletaOut]:

    query = select(AtletaModel)

    if nome:
        query = query.filter(AtletaModel.nome.ilike(f'%{nome}%'))

    if cpf:
        query = query.filter_by(cpf=cpf)

    return await paginate_sqlalchemy(db_session, query) 