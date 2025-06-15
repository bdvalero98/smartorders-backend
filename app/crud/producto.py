from sqlalchemy.orm import Session

from app.core.exceptions import handle_db_exceptions
from app.models.producto import Producto
from app.schemas.producto import ProductoCreate


def get_productos(db: Session):
    try:
        return db.query(Producto).all()
    except Exception as e:
        return handle_db_exceptions(e)


def get_producto(db: Session, producto_id: int):
    try:
        return db.query(Producto).filter(Producto.id == producto_id).first()
    except Exception as e:
        return handle_db_exceptions(e)


def create_producto(db: Session, producto: ProductoCreate):
    try:
        db_producto = Producto(**producto.model_dump())
        db.add(db_producto)
        db.commit()
        db.refresh(db_producto)
        return db_producto
    except Exception as e:
        return handle_db_exceptions(e)
