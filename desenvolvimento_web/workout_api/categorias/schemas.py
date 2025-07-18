from typing import Annotated

from pydantic import Field
from desenvolvimento_web.workout_api.contrib.schemas import BaseSchema

class Categoria(BaseSchema):

    nome: Annotated[str, Field(description='Nome da Categoria', example='Atletismo', max_length=10)]
    