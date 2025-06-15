from sqlalchemy.orm import Session

from app.models.producto import Producto
from app.schemas.producto import ProductoCreate


def get_productos(db: Session):
    return db.query(Producto).all()


def get_producto(db: Session, producto_id: int):
    return db.query(Producto).filter(Producto.id == producto_id).first()


def create_producto(db: Session, producto: ProductoCreate):
    db_producto = Producto(**producto.model_dump())
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto
