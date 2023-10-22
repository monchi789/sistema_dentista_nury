from pydantic import BaseModel


class ContrasenaRequest(BaseModel):

    contrasena: str
    nueva_contrasena: str

    class Config:
        json_schema_extra = {
            'example': {
                'contrasena': '1234',
                'nueva_contrasena': '12345@'
            }
        }