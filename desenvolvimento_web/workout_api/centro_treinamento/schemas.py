from typing import Annotated

from pydantic import Field
from desenvolvimento_web.workout_api.contrib.schemas import BaseSchema

class CentroTreinamento(BaseSchema):

    nome: Annotated[str, Field(description='Nome do Centro de Treinamento', example='Mineirao', max_length=20)]
    endereco: Annotated[str, Field(description='Endereço do Centro de Treinamento', example='Rua X, 202', max_length=60)]
    proprietario: Annotated[str, Field(description='Proprietario do Centro de Treinamento', example='Nicolas', max_length=30)]
    