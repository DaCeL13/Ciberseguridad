# Esta excepción se lanzará cuando no se encuentre un recurso
class NotFoundException(Exception):
    def __init__(self, message: str = "Recurso no encontrado"):
        self.message = message
# Esta excepción se lanzará cuando no se pueda establecer una conexión con la base de datos
class DatabaseConnectionException(Exception):
    def __init__(self, message: str = "Error al conectar con la base de datos"):
        self.message = message

class ConflictException(Exception):
    def __init__(self, message: str = "Conflicto de datos"):
        self.message = message
