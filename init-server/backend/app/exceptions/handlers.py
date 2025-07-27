from fastapi import Request, status
from fastapi.responses import JSONResponse
from app.exceptions.custom_exceptions import NotFoundException, DatabaseConnectionException, ConflictException

# Estructura para la excepción NotFoundException
def not_found_exception_handler(request: Request, exc: NotFoundException):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            "status": "error",
            "message": exc.message,
            "data": None
        }
    )
# Estructura para la excepción DatabaseConnectionException
def db_connection_exception_handler(request: Request, exc: DatabaseConnectionException):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "status": "error",
            "message": exc.message,
            "data": None
        }
    )
# Estructura para la excepción ConflictException
def conflict_exception_handler(request: Request, exc: ConflictException):
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={
            "status": "error",
            "message": exc.message,
            "data": None
        }
    )