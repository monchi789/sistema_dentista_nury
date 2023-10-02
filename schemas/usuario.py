from pydantic import BaseModel, Field
from typing import Optional


class UsuarioRequest(BaseModel):

    usuario: str
    telefono: Optional[str] = None
    correo: str
    nombres: str
    apellidos: str
    contrasena: str = Field(min_length=3)
    rol: str

    class Config:
        json_schema_extra = {
            'example' : {
                'usuario': 'example',
                'telefono': '999999999',
                'correo': 'example@example.com',
                'nombres': 'examples',
                'apellidos': 'examples',
                'contrasena': '1234',
                'rol': 'usuario'
            }
        }
