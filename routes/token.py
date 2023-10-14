from datetime import datetime, timedelta
from typing import Annotated
from fastapi import Depends, APIRouter, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from config.database import db_dependency
from models.usuario import Usuarios
from passlib.context import CryptContext


router = APIRouter(
    tags=['Token']
)


bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
form_data_dependency = Annotated[OAuth2PasswordRequestForm, Depends()]


def authenticate_user(usuario: str, contrasena: str, db):
    usuario = db.query(Usuarios).filter(Usuarios.usuario == usuario).first()

    if not usuario:
        return False
    if not bcrypt_context.verify(contrasena, usuario.contrasena):
        return False
    
    return usuario


@router.post('/token', status_code=status.HTTP_201_CREATED)
async def login_for_access_token(form_data: form_data_dependency, db: db_dependency):
    
    usuario = authenticate_user(form_data.username, form_data.password, db)

    if not usuario:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZE, detail='Usuario no valido')
    
    # token = 