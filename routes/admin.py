from fastapi import APIRouter, HTTPException, status, Path
from routes.token import user_dependecy
from models.usuario import Usuarios
from config.database import db_dependency


router = APIRouter(
    tags=['Administrador'],
    prefix='/admin'
)


@router.get('/usuarios/', status_code=status.HTTP_200_OK)
async def get_all_usuarios(usuario: user_dependecy, db: db_dependency):

    if usuario is None or usuario.get('rol') == 'admin':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Autenticacion Fallida 😄')

    return db.query(Usuarios).all()


@router.delete('/usuarios/{usuario_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_usuario(usuario: user_dependecy, db: db_dependency, usuario_id: int = Path(gt=0)):

    if usuario is None or usuario.get('rol') == 'admin':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Autenticacion Fallida')

    usuario_model = db.query(Usuarios).filter(Usuarios.id == usuario_id).first()

    if usuario_model is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Usuario no encontrado')
    
    db.query(Usuarios).filter(Usuarios.id == usuario_id).delete()
    db.commit()
