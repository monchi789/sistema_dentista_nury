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