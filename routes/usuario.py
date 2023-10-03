from fastapi import APIRouter, status, HTTPException, Path
from config.database import db_dependency
from models.usuario import Usuarios
from schemas.usuario import UsuarioRequest



router = APIRouter(
    tags=['Usuarios']
)


@router.get('/usuarios', status_code=status.HTTP_200_OK)
async def get_all_users(db: db_dependency):
    
    return db.query(Usuarios).all()


@router.get('/usuarios/{usuario_id}', status_code=status.HTTP_200_OK)
async def get_user_by_id(db: db_dependency, usuario_id: int = Path(gt=0)):

    return db.query(Usuarios).filter(Usuarios.id == usuario_id).first()


# @router.post('/usuarios')