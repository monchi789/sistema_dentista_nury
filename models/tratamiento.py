from config.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float


class Tratamientos(Base):

    __tablename__ = 'tratamientos'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    descripcion = Column(String)
    costo_total = Column(Float)
    monto_pagado = Column(Float, default=0)

    id_paciente = Column(Integer, ForeignKey('pacientes.id'))
    