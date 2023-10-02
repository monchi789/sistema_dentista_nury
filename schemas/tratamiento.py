from pydantic import BaseModel
from typing import Optional

class TratamientoRequest(BaseModel):

    nombre: str
    descripcion: Optional[str] = None
    costo_total: float
    monto_pagado: float
    id_paciente: int

    class Config:
        json_schema_extra = {
            'example': {
                'nombre': 'Ortodoncia',
                'descripcion': 'Este tratamiento es una ortodoncia',
                'costo_total': 2500.00,
                'monto_pagado': 1400.00,
                'id_paciente': 1
            }
        }
        