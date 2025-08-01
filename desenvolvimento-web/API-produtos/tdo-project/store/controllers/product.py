from typing import List, Optional
from fastapi import APIRouter, Body, Depends, HTTPException, Path, Query, status
from pydantic import UUID4
from store.core.exceptions import NotFoundException, ErrorInsert

from store.schemas.product import ProductIn, ProductOut, ProductUpdate, ProductUpdateOut
from store.usecases.product import ProductUsecase

router = APIRouter(tags=["products"])

@router.post(
        summary= "Criar Produto",
        path="/",
        status_code=status.HTTP_201_CREATED
    )
async def post(
    body: ProductIn = Body(...), 
    usecase: ProductUsecase = Depends()
    ) -> ProductOut:
    try:
        return await usecase.create(body=body)
    except ErrorInsert as exc:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=exc.message) 


@router.get(
        summary="Consultar um produto",
        path="/{id}", 
        status_code=status.HTTP_200_OK
        )
async def get(
    id: UUID4 = Path(alias="id"), usecase: ProductUsecase = Depends()
) -> ProductOut:
    try:
        return await usecase.get(id=id)
    except NotFoundException as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=exc.message)


@router.get(
    summary="Consultar todos os produtos ou filtrar pelo preço",
    path="/", 
    status_code=status.HTTP_200_OK)
async def query(
    usecase: ProductUsecase = Depends(),
    min_price: Optional[float] = Query(None, description="Preço minimo do produto"),
    max_price: Optional[float] = Query(None, description="Preço máximo do produto")
    ) -> List[ProductOut]:
    return await usecase.query(min_price=min_price,max_price=max_price)


@router.patch(
        summary= "Atualizar um Produto",
        path="/{id}", 
        status_code=status.HTTP_200_OK
        )
async def patch(
    id: UUID4 = Path(alias="id"),
    body: ProductUpdate = Body(...),
    usecase: ProductUsecase = Depends(),
) -> ProductUpdateOut:
    try:
        return await usecase.update(id=id, body=body)
    except NotFoundException as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=exc.message)


@router.delete(
        summary="Deletar um Produto",
        path="/{id}", 
        status_code=status.HTTP_204_NO_CONTENT
        )
async def delete(
    id: UUID4 = Path(alias="id"), usecase: ProductUsecase = Depends()
) -> None:
    try:
        await usecase.delete(id=id)
    except NotFoundException as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=exc.message)