from pydantic import BaseModel


class PagoRequest(BaseModel):

    monto: float
    fecha_pago: str
    id_tratamiento: int

    class Config:
        json_schema_extra = {
            'example': {
                'monto': 100.00,
                'fecha_pago': '2023-12-25',
                'id_tratamiento': 1
            }
        }
        