from fastapi import APIRouter, status, HTTPException, Path
from config.database import db_dependency
from models.paciente import Pacientes
from schemas.paciente import PacienteRequest
from routes.token import user_dependecy


router = APIRouter(
    tags=['Pacientes']
)


@router.get('/pacientes', status_code=status.HTTP_200_OK)
async def get_all_pacientes(usuario: user_dependecy, db: db_dependency):
    return db.query(Pacientes).filter(Pacientes.id_usuario == usuario.get('id')).all()


@router.get('/pacientes/{paciente_id}', status_code=status.HTTP_200_OK)
async def get_all_pacientes_by_id(usuario: user_dependecy, db: db_dependency, paciente_id: int = Path(gt=0)):
    
    return db.query(Pacientes).filter(Pacientes.id == paciente_id).filter(Pacientes.id_usuario == usuario.get('id')).first()


@router.post('/pacientes', status_code=status.HTTP_201_CREATED)
async def create_paciente(usuario: user_dependecy, db: db_dependency, paciente_request: PacienteRequest):
    
    if usuario is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Fallo de authenticacion')

    paciente_model = Pacientes(
        nombres=paciente_request.nombres, apellidos=paciente_request.apellidos, 
        telefono=paciente_request.telefono, id_usuario=usuario.get('id')
    )

    db.add(paciente_model)
    db.commit()


@router.put('/pacientes/{paciente_id}', status_code=status.HTTP_204_NO_CONTENT)
async def update_paciente(usuario: user_dependecy, db: db_dependency, paciente_request: PacienteRequest, paciente_id: int = Path(gt=0)):
    
    paciente_model = db.query(Pacientes).filter(Pacientes.id == paciente_id).filter(Pacientes.id_usuario == usuario.get('id')).first()

    if paciente_model is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Paciente no encontrado')
    
    paciente_model.nombres = paciente_request.nombres
    paciente_model.apellidos = paciente_request.apellidos
    paciente_model.telefono = paciente_request.telefono
    paciente_model.id_usuario = usuario.get('id')

    db.add(paciente_model)
    db.commit()


@router.delete('/pacientes/{pacientes_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_pacientes(usuario: user_dependecy, db: db_dependency, pacientes_id: int = Path(gt=0)):

    if usuario is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Falla de authenticacion')
    

    paciente_model = db.query(Pacientes).filter(Pacientes.id == pacientes_id).filter(Pacientes.id_usuario == usuario.get('id')).first()

    if paciente_model is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Paciente no encontrado')

    db.query(Pacientes).filter(Pacientes.id == pacientes_id).delete()
    db.commit()
    