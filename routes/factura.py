from fastapi import APIRouter, Path, status, HTTPException
from models.factura import Facturas
from schemas.factura import FacturaRequest
from config.database import db_dependency
from datetime import datetime


router = APIRouter(
    tags=['Facturas']
)


@router.get('/facturas', status_code=status.HTTP_200_OK)
async def get_all_facturas(db: db_dependency): 

    return db.query(Facturas).all()


@router.get('/factura/{factura_id}', status_code=status.HTTP_200_OK)
async def get_factura_by_id(db: db_dependency, factura_id: int = Path(gt=0)):

    return db.query(Facturas).filter(Facturas.id == factura_id).first


@router.post('/facturas', status_code=status.HTTP_201_CREATED)
async def create_facturas(db: db_dependency, factura_request: FacturaRequest):

    factura_model = Facturas(**factura_request.model_dump())

    db.add(factura_model)
    db.commit()


@router.put('/factura/{factura_id}', status_code=status.HTTP_204_NO_CONTENT)
async def update_factura(db: db_dependency, factura_request: FacturaRequest, factura_id: int = Path(gt=0)):
    factura_model = db.query(Facturas).filter(Facturas.id == factura_id).first()

    if factura_model is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Factura no encontrada')
    
    factura_model.total = factura_request.total
    factura_model.fecha_emision = datetime.strptime(factura_request.fecha_emision, '%Y-%m-%d')
    factura_model.id_tratamiento = factura_request.id_tratamiento

    db.add(factura_model)
    db.commit()


@router.delete('/factura/{factura_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_factura(db: db_dependency, factura_id: int = Path(gt=0)):
    
    db.query(Facturas).filter(Facturas.id == factura_id).delete()
    db.commit()
