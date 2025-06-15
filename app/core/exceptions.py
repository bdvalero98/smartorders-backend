from sqlalchemy.exc import SQLAlchemyError, IntegrityError


class DatabaseException(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


def handle_db_exceptions(error: Exception):
    if isinstance(error, IntegrityError):
        raise DatabaseException("Error de integridad en la base de datos")
    elif isinstance(error, SQLAlchemyError):
        raise DatabaseException("Error interno de base de datos")
    else:
        raise DatabaseException("Error inesperado en la base de datos")
