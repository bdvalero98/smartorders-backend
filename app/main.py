from fastapi import FastAPI

from app.api.v1 import routes_producto
from app.api.v1 import routes_root
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION
)

# Incluir rutas
app.include_router(routes_root.router)
app.include_router(routes_producto.router, prefix="/api/v1")
