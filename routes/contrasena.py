from fastapi import APIRouter, HTTPException, status
from routes.token import user_dependecy
from config.database import db_dependency
from schemas.contrasena import ContrasenaRequest
from models.usuario import Usuarios
from passlib.context import CryptContext


router = APIRouter(
    tags=['Contrasena']
)


bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


@router.put('/password', status_code=status.HTTP_204_NO_CONTENT)
async def cambiar_contrasena(usuario: user_dependecy, db: db_dependency, contrasena: ContrasenaRequest):

    if usuario is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Autenticacion Fallida')
    
    usuario_model = db.query(Usuarios).filter(Usuarios.id == usuario.get('id')).first()

    if not bcrypt_context.verify(contrasena.contrasena, usuario_model.contrasena):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Falla al cambiar contrasena')

    usuario_model.contrasena = bcrypt_context.hash(contrasena.nueva_contrasena)

    db.add(usuario_model)
    db.commit()