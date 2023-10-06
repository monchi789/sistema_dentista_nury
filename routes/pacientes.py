from fastapi import APIRouter, status, HTTPException, Path
from config.database import db_dependency
from models.paciente import Pacientes
from schemas.paciente import PacienteRequest


router = APIRouter(
    tags=['Pacientes']
)


@router.get('/pacientes', status_code=status.HTTP_200_OK)
async def get_all_pacientes(db: db_dependency):

    return db.query(Pacientes).all()


@router.get('/pacientes/{paciente_id}', status_code=status.HTTP_200_OK)
async def get_all_pacientes_by_id(db: db_dependency, paciente_id: int = Path(gt=0)):
    return db.query(Pacientes).filter(Pacientes.id == paciente_id).first()


@router.post('/pacientes', status_code=status.HTTP_201_CREATED)
async def create_paciente(db: db_dependency, paciente_request: PacienteRequest):
    
    paciente_model = Pacientes(**paciente_request.model_dump())

    db.add(paciente_model)
    db.commit()


@router.put('/pacientes/{paciente_id}', status_code=status.HTTP_204_NO_CONTENT)
async def update_paciente(db: db_dependency, paciente_request: PacienteRequest, paciente_id: int = Path(gt=0)):
    
    paciente_model = db.query(Pacientes).filter(Pacientes.id == paciente_id).first()

    if paciente_model is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Paciente no encontrado')
    
    paciente_model.nombres = paciente_request.nombres
    paciente_model.apellidos = paciente_request.apellidos
    paciente_model.telefono = paciente_request.telefono
    paciente_model.id_usuario = paciente_request.id_usuario

    db.add(paciente_model)
    db.commit()


@router.delete('/pacientes/{pacientes_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_pacientes(db: db_dependency, pacientes_id: int = Path(gt=0)):

    db.query(Pacientes).filter(Pacientes.id == pacientes_id).first()
    db.commit()
    