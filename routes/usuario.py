from fastapi import APIRouter, status, HTTPException, Path
from config.database import db_dependency
from models.usuario import Usuarios
from schemas.usuario import UsuarioRequest
from passlib.context import CryptContext


router = APIRouter(
    tags=['Usuarios']
)


@router.get('/usuarios', status_code=status.HTTP_200_OK)
async def get_all_usuarios(db: db_dependency):
    
    return db.query(Usuarios).all()


@router.get('/usuarios/{usuario_id}', status_code=status.HTTP_200_OK)
async def get_usuario_by_id(db: db_dependency, usuario_id: int = Path(gt=0)):

    return db.query(Usuarios).filter(Usuarios.id == usuario_id).first()


@router.post('/usuarios', status_code=status.HTTP_201_CREATED)
async def create_usuario(db: db_dependency, usuario_request: UsuarioRequest):
    
    usuario_model = Usuarios(
        usuario=usuario_request.usuario, telefono=usuario_request.telefono, correo=usuario_request.correo, 
        nombres=usuario_request.nombres, apellidos=usuario_request.apellidos, contrasena=usuario_request.contrasena,
        rol=usuario_request.rol
    )

    db.add(usuario_model)
    db.commit()


@router.put('/usuarios/{usuario_id}', status_code=status.HTTP_204_NO_CONTENT)
async def update_usuario(db: db_dependency, usuario_request: UsuarioRequest, usuario_id: int = Path(gt=0)):
    
    usuario_model = db.query(Usuarios).filter(Usuarios.id == usuario_id).first()

    if usuario_model is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Ususario no encontrado')
    
    usuario_model.usuario = usuario_request.usuario
    usuario_model.telefono = usuario_request.telefono
    usuario_model.correo = usuario_request.correo
    usuario_model.nombres = usuario_request.nombres
    usuario_model.apellidos = usuario_request.apellidos
    usuario_model.contrasena = usuario_request.contrasena
    usuario_model.rol = usuario_request.rol

    db.add(usuario_model)
    db.commit()


@router.delete('/usuarios/{usuario_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_usuario(db: db_dependency, usuario_id: int = Path(gt=0)):

    usuario_model = db.query(Usuarios).filter(Usuarios.id == usuario_id).first()

    if usuario_model is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Usuario no encontrado')
    
    db.query(Usuarios).filter(Usuarios.id == usuario_id).delete()
    db.commit()
