from fastapi import APIRouter, Path, status, HTTPException
from models.factura import Facturas
from schemas.factura import FacturaRequest
from config.database import db_dependency


router = APIRouter(
    tags=['Facturas']
)


@router.get('/facturas', status_code=status.HTTP_200_OK)
async def get_all_facturas(db: db_dependency): 
    return db.query(Facturas).all()