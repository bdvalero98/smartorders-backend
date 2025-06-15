class DatabaseException(Exception):
    """Excepcion personalizada para errores de base de datos"""
    def __init__(self, message: str = "Error interno de base de datos"):
        self.message = message
        super().__init__(self.message)