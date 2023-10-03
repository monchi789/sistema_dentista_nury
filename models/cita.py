from config.database import Base
from sqlalchemy import ForeignKey, Date, Time, Integer, Column, String


class Citas(Base):

    __tablename__ = 'citas'

    id = Column(Integer, primary_key=True, index=True)
    fecha = Column(Date)
    hora = Column(Time)
    descripcion = Column(String)

    id_paciente = Column(Integer, ForeignKey('pacientes.id'))
