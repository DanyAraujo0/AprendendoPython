from uuid import uuid4
from fastapi import APIRouter, Body, status, HTTPException
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate as paginate_sqlalchemy
from pydantic import UUID4
from workout_api.centro_treinamento.models import CentroTreinamentoModel
from workout_api.centro_treinamento.schemas import CentroTreinamentoIn, CentroTreinamentoOut
from workout_api.contrib.dependencies import DatabaseDependency
from sqlalchemy.future import select

router = APIRouter()

@router.post(
        '/',
        summary='Criar um novo Centro de Treinamento',
        status_code=status.HTTP_201_CREATED,
        response_model=CentroTreinamentoOut,
)
async def post(
    db_session: DatabaseDependency,
    centro_treinamento_in: CentroTreinamentoIn = Body(...)
    ) -> CentroTreinamentoOut:

    centro_treinamento_out = CentroTreinamentoOut(id=uuid4(), **centro_treinamento_in.model_dump())
    centro_treinamento_model = CentroTreinamentoModel(**centro_treinamento_out.model_dump())

    db_session.add(centro_treinamento_model)
    await db_session.commit()       

    return centro_treinamento_out

@router.get(
        '/',
        summary='Consultar todos os Centros de Treinamentos',
        status_code=status.HTTP_200_OK,
        response_model=Page[CentroTreinamentoOut],
)
async def query(db_session: DatabaseDependency)->Page[CentroTreinamentoOut]:

    return await paginate_sqlalchemy(db_session, select(CentroTreinamentoModel))

@router.get(
        '/{id}',
        summary='Consultar um Centro de Treinamento pelo id',
        status_code=status.HTTP_200_OK,
        response_model=CentroTreinamentoOut,
)
async def query(id: UUID4 ,db_session: DatabaseDependency)->list[CentroTreinamentoOut]:
    centro_treinamento: CentroTreinamentoOut = (
        await db_session.execute(select(CentroTreinamentoModel).filter_by(id=id))
        ).scalars().first()
    if not centro_treinamento:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND, 
            detail=f'Centro de Treinamento não encontrado no id {id}'
            )

    return centro_treinamento