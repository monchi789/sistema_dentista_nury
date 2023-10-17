from fastapi import APIRouter, HTTPException, status, Path
from models.tratamiento import Tratamientos
from schemas.tratamiento import TratamientoRequest
from config.database import db_dependency
from routes.token import user_dependecy


router = APIRouter(
    tags=['Tratamientos']
)


@router.get('/tratamientos', status_code=status.HTTP_200_OK)
async def get_all_tratamientos(usuario: user_dependecy, db: db_dependency):
    
    if usuario is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Autenticacion Fallida')

    return db.query(Tratamientos).all()


@router.get('/tratamiento/{tratamiento_id}', status_code=status.HTTP_200_OK)
async def get_tratamiento_by_id(usuario: user_dependecy, db: db_dependency, tratamiento_id: int = Path(gt=0)):
    
    if usuario is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Autenticacion Fallida')

    return db.query(Tratamientos).filter(Tratamientos.id == tratamiento_id).first()


@router.post('/tratamientos', status_code=status.HTTP_201_CREATED)
async def create_tratamiento(usuario: user_dependecy, db: db_dependency, tratamiento_request: TratamientoRequest):

    if usuario is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Autenticacion Fallida')

    tratamiento_model = Tratamientos(**tratamiento_request.model_dump())

    db.add(tratamiento_model)
    db.commit()


@router.put('/tratamiento/{tratamiento_id}', status_code=status.HTTP_204_NO_CONTENT)
async def update_tratamiento(usuario: user_dependecy, db: db_dependency, tratamiento_request: TratamientoRequest, tratamiento_id: int = Path(gt=0)):

    if usuario is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Autenticacion Fallida')

    tratamiento_model = db.query(Tratamientos).filter(Tratamientos.id == tratamiento_id).first()

    if tratamiento_model is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Tratamiento no encontrado')
    
    tratamiento_model.nombre = tratamiento_request.nombre
    tratamiento_model.descripcion = tratamiento_request.descripcion
    tratamiento_model.costo_total = tratamiento_request.costo_total
    tratamiento_model.monto_pagado = tratamiento_request.monto_pagado


    db.add(tratamiento_model)
    db.commit()


@router.delete('/tratamiento/{tratamiento_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_tratamiento(usuario: user_dependecy, db: db_dependency, tratamiento_id: int = Path(gt=0)):
    
    if usuario is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Autenticacion Fallida')

    db.query(Tratamientos).filter(Tratamientos.id == tratamiento_id).delete()
    db.commit()