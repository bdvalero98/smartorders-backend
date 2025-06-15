from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.core.exceptions import DatabaseException
from app.crud import producto as crud_producto
from app.schemas.producto import ProductoCreate, ProductoOut

router = APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/productos", response_model=List[ProductoOut])
def listar_productos(db: Session = Depends(get_db)):
    try:
        return crud_producto.get_productos(db)
    except DatabaseException as e:
        raise HTTPException(status_code=500, detail=e.message)


@router.get("/productos/{producto_id}", response_model=ProductoOut)
def obtener_producto(producto_id: int, db: Session = Depends(get_db)):
    try:
        db_producto = crud_producto.get_producto(db, producto_id)
        if not db_producto:
            raise HTTPException(status_code=404, detail="Producto no encontrado")
        return db_producto
    except DatabaseException as e:
        raise HTTPException(status_code=500, detail=e.message)


@router.post("/productos", response_model=ProductoOut, status_code=201)
def crear_producto(producto: ProductoCreate, db: Session = Depends(get_db)):
    try:
        return crud_producto.create_producto(db, producto)
    except DatabaseException as e:
        raise HTTPException(status_code=500, detail=e.message)
