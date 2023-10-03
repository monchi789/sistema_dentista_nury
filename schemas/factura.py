from pydantic import BaseModel


class FacturaRequest(BaseModel):

    total: float
    fecha_emision: str
    id_tratamiento: int

    class Config:
        json_schema_extra = {
            'example': { 
                'total': 100.00,
                'fecha_emision': '2023-10-2',
                'id_tratamiento': 1
            }
        }
