from fastapi import APIRouter, Path, status, HTTPException
from models.factura import Facturas
from schemas.factura import FacturaRequest
from config.database import db_dependency
from datetime import datetime
from routes.token import user_dependecy


router = APIRouter(
    tags=['Facturas']
)


@router.get('/facturas', status_code=status.HTTP_200_OK)
async def get_all_facturas(usuario: user_dependecy, db: db_dependency): 

    if usuario is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Autenticacion Fallida')

    return db.query(Facturas).all()


@router.get('/factura/{factura_id}', status_code=status.HTTP_200_OK)
async def get_factura_by_id(usuario: user_dependecy, db: db_dependency, factura_id: int = Path(gt=0)):

    if usuario is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Autenticacion Fallida')

    return db.query(Facturas).filter(Facturas.id == factura_id).first


@router.post('/facturas', status_code=status.HTTP_201_CREATED)
async def create_facturas(usuario: user_dependecy, db: db_dependency, factura_request: FacturaRequest):

    if usuario is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Autenticacion Fallida')

    factura_model = Facturas(**factura_request.model_dump())

    db.add(factura_model)
    db.commit()


@router.put('/factura/{factura_id}', status_code=status.HTTP_204_NO_CONTENT)
async def update_factura(usuario: user_dependecy, db: db_dependency, factura_request: FacturaRequest, factura_id: int = Path(gt=0)):

    if usuario is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Autenticacion Fallida')

    factura_model = db.query(Facturas).filter(Facturas.id == factura_id).first()

    if factura_model is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Factura no encontrada')
    
    factura_model.total = factura_request.total
    factura_model.fecha_emision = datetime.strptime(factura_request.fecha_emision, '%Y-%m-%d')
    factura_model.id_tratamiento = factura_request.id_tratamiento

    db.add(factura_model)
    db.commit()


@router.delete('/factura/{factura_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_factura(usuario: user_dependecy, db: db_dependency, factura_id: int = Path(gt=0)):

    if usuario is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Autenticacion Fallida')    
    
    db.query(Facturas).filter(Facturas.id == factura_id).delete()
    db.commit()
