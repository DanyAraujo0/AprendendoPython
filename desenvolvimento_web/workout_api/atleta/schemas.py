from typing import Annotated
from pydantic import BaseModel, Field, PositiveFloat

from desenvolvimento_web.workout_api.contrib.schemas import BaseSchema

class Atleta(BaseSchema):
    nome: Annotated[str, Field(description='Nome do atleta', example='Joao', max_length=50)]
    cpf: Annotated[str, Field(description='CPF do atleta', example='12345678900', max_length=11)]
    idade: Annotated[int, Field(description='Idade do atleta', example=25)]
    peso: Annotated[PositiveFloat, Field(description='Peso do atleta', example=80.10)]
    altura: Annotated[PositiveFloat, Field(description='Altura do atleta', example=188.77)]
    sexo: Annotated[str, Field(description='Sexo do atleta',example='M', max_length=1)]