from pydantic import BaseModel


class Token(BaseModel):

    acceso_token: str
    tipo_token: str
