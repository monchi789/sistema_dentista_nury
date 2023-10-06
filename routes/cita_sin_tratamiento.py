from fastapi import APIRouter, status, Path, HTTPException
from config.database import db_dependency
from schemas.cita_sin_tratamiento import CitaSinTratamientoRequest
from models.cita_sin_tratamiento import CitasSinTratamiento
from datetime import datetime


router = APIRouter(
    tags=['Cita Sin Tratamientos']
)


@router.get('/citas_sin_tratamiento', status_code=status.HTTP_200_OK)
async def get_all_citas_sin_tratamiento(db: db_dependency):
    
    return db.query(CitasSinTratamiento).all()


@router.get('/citas_sin_tratamiento/{cita_sin_tratamiento_id}', status_code=status.HTTP_200_OK)
async def get_cita_sin_tratamiento_by_id(db: db_dependency, cita_sin_tratamiento_id: int = Path(gt=0)):
    
    return db.query(CitasSinTratamiento).filter(CitasSinTratamiento.id == cita_sin_tratamiento_id).first()

@router.post('/citas_sin_tratamiento', status_code=status.HTTP_201_CREATED)
async def crete_cita_sin_tratamiento(db: db_dependency, cita_sin_tratamiento_request: CitaSinTratamientoRequest):
    
    cita_sin_tratamiento_model = CitasSinTratamiento(**cita_sin_tratamiento_request.model_dump())

    db.add(cita_sin_tratamiento_model)
    db.commit() 


@router.put('/citas_sin_tratamiento/{cita_sin_tratamiento_id}', status_code=status.HTTP_204_NO_CONTENT)
async def update_cita_sin_tratamiento(db: db_dependency, cita_sin_tratamiento_resquest: CitaSinTratamientoRequest, cita_sin_tratamiento_id: int = Path(gt=0)):

    cita_sin_tratamiento_model = db.query(CitasSinTratamiento).filter(CitasSinTratamiento.id == cita_sin_tratamiento_id).first()

    if cita_sin_tratamiento_model is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Usuario no encontrado')

    cita_sin_tratamiento_model.fecha = datetime.strptime(cita_sin_tratamiento_resquest.fecha, '%Y-%m-%d')
    cita_sin_tratamiento_model.hora = datetime.strptime(cita_sin_tratamiento_resquest.hora, '%H:%M:%S').time()
    cita_sin_tratamiento_model.descripcion = cita_sin_tratamiento_resquest.descripcion
    cita_sin_tratamiento_model.monto = cita_sin_tratamiento_resquest.monto

    db.add(cita_sin_tratamiento_model)
    db.commit()


@router.delete('/citas_sin_tratamiento/{citas_sin_tratamiento_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_usuario(db: db_dependency, citas_sin_tratamiento_id: int = Path(gt=0)):

    db.query(CitasSinTratamiento).filter(CitasSinTratamiento.id == citas_sin_tratamiento_id).delete()
    db.commit()
