# Esta excepción se lanzará cuando no se encuentre un recurso
class NotFoundException(Exception):
    def __init__(self, name: str):
        self.name = name
# Esta excepción se lanzará cuando no se pueda establecer una conexión con la base de datos        
class DatabaseConnectionException(Exception):
    def __init__(self, message: str = "Error al conectar con la base de datos"):
        self.message = message
