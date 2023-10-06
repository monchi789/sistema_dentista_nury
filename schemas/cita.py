from pydantic import BaseModel


class CitaRequest(BaseModel):

    fecha: str
    hora: str
    descripcion: str
    id_paciente: int

    class Config:
        json_schema_extra = {
            'example': {
                'fecha': '2020-11-24',
                'hora': '15:35:00',
                'descripcion': 'Esto fue una  cita ',
                'id_paciente': 1
            }
        }