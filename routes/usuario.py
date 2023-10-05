from fastapi import APIRouter, status, HTTPException, Path
from config.database import db_dependency
from models.usuario import Usuarios
from schemas.usuario import UsuarioRequest
from passlib.context import CryptContext


router = APIRouter(
    tags=['Usuarios']
)


@router.get('/usuarios', status_code=status.HTTP_200_OK)
async def get_all_users(db: db_dependency):
    
    return db.query(Usuarios).all()


@router.get('/usuarios/{usuario_id}', status_code=status.HTTP_200_OK)
async def get_user_by_id(db: db_dependency, usuario_id: int = Path(gt=0)):

    return db.query(Usuarios).filter(Usuarios.id == usuario_id).first()


@router.post('/usuarios', status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency, user_request: UsuarioRequest):
    
    user_model = Usuarios(
        usuario=user_request.usuario, telefono=user_request.telefono, correo=user_request.correo, 
        nombres=user_request.nombres, apellidos=user_request.apellidos, contrasena=user_request.contrasena,
        rol=user_request.rol
    )

    db.add(user_model)
    db.commit()


@router.put('/usuarios/{usuario_id}', status_code=status.HTTP_204_NO_CONTENT)
async def update_user(db: db_dependency, user_request: UsuarioRequest, usuario_id: int = Path(gt=0)):
    
    user_model = db.query(Usuarios).filter(Usuarios.id == usuario_id).first()

    if user_model is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Ususario no encontrado')
    
    user_model.usuario = user_request.usuario
    user_model.telefono = user_request.telefono
    user_model.correo = user_request.correo
    user_model.nombres = user_request.nombres
    user_model.apellidos = user_request.apellidos
    user_model.contrasena = user_request.contrasena
    user_model.rol = user_request.rol

    db.add(user_model)
    db.commit()


@router.delete('/usuarios/{usuario_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(db: db_dependency, usuario_id: int = Path(gt=0)):

    user_model = db.query(Usuarios).filter(Usuarios.id == usuario_id).first()

    if user_model is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Usuario no encontrado')
    
    db.query(Usuarios).filter(Usuarios.id == usuario_id).delete()
    db.commit()
