from config.database import Base
from sqlalchemy import Date, Float, Integer, ForeignKey, Column


class Factura(Base):

    __tablename__ = 'facturas'

    id = Column(Integer, primary_key=True, index=True)
    total = Column(Float)
    fecha_emision = Column(Date)

    id_tratamiento = Column(Integer, ForeignKey('tratamientos.id'))