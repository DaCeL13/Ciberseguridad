from fastapi import Request
from fastapi.responses import JSONResponse
from app.exceptions.custom_exceptions import NotFoundException, DatabaseConnectionException

# Estructura para la excepción NotFoundException
def not_found_exception_handler(request: Request, exc: NotFoundException):
    return JSONResponse(
        status_code=404,
        content={
            "status": "error",
            "message": f"{exc.name} not found",
            "data": None
        }
    )
# Estructura para la excepción DatabaseConnectionException
def db_connection_exception_handler(request: Request, exc: DatabaseConnectionException):
    return JSONResponse(
        status_code=500,
        content={
            "status": "error",
            "message": exc.message,
            "data": None
        }
    )
