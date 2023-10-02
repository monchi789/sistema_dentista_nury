from pydantic import BaseModel
from typing import Optional


class PacienteRequest(BaseModel):

    nombres: str
    apellidos: str
    telefono: Optional[str] = None
    id_usuario: int

    class Config:
        json_schema_extra = {
            'example': {
                'nombres': 'Nick',
                'apellidos': 'Mendoza',
                'telefono': '999999999',
                'id_usuario': 1
            }
        }
