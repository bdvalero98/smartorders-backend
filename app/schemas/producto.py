from pydantic import BaseModel, ConfigDict


class ProductoBase(BaseModel):
    nombre: str
    descripcion: str
    precio: float
    cantidad: int


class ProductoCreate(ProductoBase):
    pass


class ProductoOut(ProductoBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
