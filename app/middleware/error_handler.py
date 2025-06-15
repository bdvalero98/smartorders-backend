import logging

from fastapi import Request
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError
from starlette.middleware.base import BaseHTTPMiddleware

from app.exceptions.database import DatabaseException

logger = logging.getLogger("smartorders")
logging.basicConfig(level=logging.INFO)


class ErrorHandlerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            response = await call_next(request)
            return response
        except DatabaseException as db_exc:
            logger.error(f"Database error: {str(db_exc)}")
            return JSONResponse(
                status_code=500,
                content={
                    "detail": "Error interno de base de datos"
                },
            )
        except SQLAlchemyError as sa_exc:
            logger.error(f"SQLAlchemy error: {str(sa_exc)}")
            return JSONResponse(
                status_code=500,
                content={
                    "detail": "Error de base de datos"
                },
            )
        except Exception as exc:
            logger.error(f"Unhaled exception: {str(exc)}")
            return JSONResponse(
                status_code=500,
                content={
                    "detail": "Error interno del servidor"
                },
            )
