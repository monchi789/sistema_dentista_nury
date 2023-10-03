from config.database import Base
from sqlalchemy import Column, Integer, String


class Usuarios(Base):
    
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, index=True)
    usuario = Column(String, unique=True)
    telefono = Column(String)
    correo = Column(String)
    nombres = Column(String)
    apellidos = Column(String)
    contrasena = Column(String)
    rol = Column(String)
