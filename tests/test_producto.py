import pytest
from httpx import AsyncClient, ASGITransport

from app.main import app


@pytest.mark.anyio
async def test_listar_productos():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get("/api/v1/productos")
    assert response.status_code == 200


@pytest.mark.anyio
async def test_crear_producto():
    producto = {
        "nombre": "Producto test",
        "descripcion": "Probando",
        "precio": 5000.0,
        "cantidad": 2
    }
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post("/api/v1/productos", json=producto)
    assert response.status_code == 201
    assert response.json()["nombre"] == producto["nombre"]
