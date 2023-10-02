from config.database import Base
from sqlalchemy import Column, Integer, ForeignKey, Date, Float


class Pago(Base):

    __tablename__ = 'pagos'

    id = Column(Integer, primary_key=True, index=True)
    monto = Column(Float)
    fecha_pago = Column(Date)

    id_tratamiento = Column(Integer, ForeignKey('tratamientos.id'))