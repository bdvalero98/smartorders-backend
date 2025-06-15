from unittest.mock import patch

import pytest
from httpx import AsyncClient, ASGITransport
from sqlalchemy.exc import SQLAlchemyError

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
        "descripcion": "Probando test",
        "precio": 1000.0,
        "cantidad": 2
    }
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post("/api/v1/productos", json=producto)
    assert response.status_code == 201
    assert response.json()["nombre"] == producto["nombre"]


@pytest.mark.anyio
async def test_crear_producto_sin_nombre():
    producto = {
        "descripcion": "Sin nombre",
        "precio": 1000.0,
        "cantidad": 2
    }
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post("/api/v1/productos", json=producto)
    assert response.status_code == 422


@pytest.mark.anyio
async def test_crear_producto_precio_invalido():
    producto = {
        "nombre": "Producto invalido",
        "descripcion": "String como precio",
        "precio": "barato",
        "cantidad": 2
    }
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post("/api/v1/productos", json=producto)
    assert response.status_code == 422


@pytest.mark.anyio
async def test_crear_producto_error_interno():
    producto = {
        "nombre": "Producto error",
        "descripcion": "Error interno",
        "precio": 1000.0,
        "cantidad": 2
    }
    with patch("app.crud.producto.create_producto") as mock_create:
        mock_create.side_effect = SQLAlchemyError("Error Forzado")
        transport = ASGITransport(app=app)
        async with AsyncClient(transport=transport, base_url="http://test") as ac:
            response = await ac.post("/api/v1/productos", json=producto)

    assert response.status_code == 500
    assert response.json()["detail"] == "Error interno de base de datos"


@pytest.mark.anyio
async def test_obtener_producto_no_existente():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post("/api/v1/productos/99999999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Producto no existente"
