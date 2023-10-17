from datetime import datetime, timedelta
from typing import Annotated
from fastapi import Depends, APIRouter, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from config.database import db_dependency
from models.usuario import Usuarios
from passlib.context import CryptContext
from jose import jwt, JWTError


router = APIRouter(
    tags=['Token']
)


SECRET_KEY = '07a3aa9227493426075548a3e6b0358f271f3646436ae4fa3e4cef442f341a12'
ALGORITHM = 'HS256'


bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='token')
form_data_dependency = Annotated[OAuth2PasswordRequestForm, Depends()]


def authenticate_user(usuario: str, contrasena: str, db):
    usuario = db.query(Usuarios).filter(Usuarios.usuario == usuario).first()

    if not usuario:
        return False
    if not bcrypt_context.verify(contrasena, usuario.contrasena):
        return False
    
    return usuario


def create_access_token(usuario: str, id_usuario: int, expires_delta: timedelta):

    encode = {'sub': usuario, 'id': id_usuario}
    expires = datetime.utcnow() + expires_delta
    encode.update({'exp': expires})

    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)


def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        usuario: str = payload.get('sub')
        usuario_id: int = payload.get('id')

        if usuario is None or usuario_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Usuaro no valido')
        
        return {'username': usuario, 'id': usuario_id}
    
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Usuario no valido')


@router.post('/token', status_code=status.HTTP_201_CREATED)
async def login_for_access_token(form_data: form_data_dependency, db: db_dependency):
    
    usuario = authenticate_user(form_data.username, form_data.password, db)

    if not usuario:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZE, detail='Usuario no valido')
    
    token = create_access_token(usuario.usuario, usuario.id, timedelta(minutes=20))

    return {'access_token': token, 'token_type': 'bearer'}


user_dependecy = Annotated[dict, Depends(get_current_user)]