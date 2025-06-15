from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError, IntegrityError


def handle_db_exceptions(error: Exception):
    if isinstance(error, IntegrityError):
        raise HTTPException(status_code=400, detail="Error de integridad en la base de datos")
    elif isinstance(error, SQLAlchemyError):
        raise HTTPException(status_code=500, detail="Error interno de base de datos")
    else:
        raise HTTPException(status_code=500, detail="Error inesperado")
