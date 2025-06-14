from sqlalchemy import Column, Integer, String, Float
from app.core.database import Base

class Producto(Base):
    __tablename__ = 'productos'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    precio = Column(Float, nullable=False)
    cantidad = Column(Integer, nullable=False)