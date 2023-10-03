from config.database import Base
from sqlalchemy import Integer, String, ForeignKey, Column, Date, Time, Float


class CitasSinTratamiento(Base):

    __tablename__ = 'citas_sin_tratamiento'
    
    id = Column(Integer, primary_key=True, index=True)
    fecha = Column(Date)
    hora = Column(Time)
    descripcion = Column(String)
    monto = Column(Float)

    id_paciente = Column(Integer, ForeignKey('pacientes.id'))
    