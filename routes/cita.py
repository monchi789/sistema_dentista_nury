from fastapi import APIRouter, Path, HTTPException, status
from models.cita import Citas
from schemas.cita import CitaRequest
from config.database import db_dependency
from datetime import datetime


router = APIRouter(
    tags=['Citas']
)


@router.get('/citas', status_code=status.HTTP_200_OK)
async def get_all_citas(db: db_dependency):

    return db.query(Citas).all()


@router.get('/citas/{citas_id}', status_code=status.HTTP_200_OK)
async def  get_citas_by_id(db: db_dependency, citas_id: int = Path(gt=0)):

    return db.query(Citas).filter(Citas.id  == citas_id).first()


@router.post('/citas', status_code=status.HTTP_201_CREATED)
async def create_citas(db: db_dependency, citas_request: CitaRequest):

    citas_model = Citas(**citas_request.model_dump())

    db.add(citas_model)
    db.commit()


@router.put('/citas/{cita_id}', status_code=status.HTTP_204_NO_CONTENT)
async def update_cita(db: db_dependency, cita_request: CitaRequest, cita_id: int = Path(gt=0)):
    cita_model = db.query(Citas).filter(Citas.id == cita_id).first()

    if cita_model is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Cita no encontrada')
    
    cita_model.fecha = datetime.strptime(cita_request.fecha, '%Y-%m-%d')
    cita_model.hora = datetime.strptime(cita_request.hora, '%H:%M:%S').time()
    cita_model.descripcion = cita_request.descripcion

    db.add(cita_model)
    db.commit()


@router.delete('/citas/{cita_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_cita(db: db_dependency, cita_id: int = Path(gt=0)):
    db.query(Citas).filter(Citas.id == cita_id).delete()
    db.commit()