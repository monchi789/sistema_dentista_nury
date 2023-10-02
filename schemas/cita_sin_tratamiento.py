from pydantic import BaseModel

class CitaSinTratamientoRequest(BaseModel):

    fecha: str
    hora: str
    descripcion: str
    monto: float
    id_paciente: int

    class Config:
        json_schema_extra = {
            'example': {
                'fecha': '2018-08-18',
                'hora': '14:30:00',
                'descripcion': 'Esto fue una cita',
                'monto': 200.00,
                'id_paciente': 1
            }
        }
