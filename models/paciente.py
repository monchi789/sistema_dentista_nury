from config.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Pacientes(Base):

    __tablename__ = 'pacientes'

    id = Column(Integer, primary_key=True, index=True)
    nombres = Column(String)
    apellidos = Column(String)
    telefono = Column(String)

    id_usuario = Column(Integer, ForeignKey('usuarios.id'))