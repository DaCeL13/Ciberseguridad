from fastapi import APIRouter
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from app.db.session import SessionLocal
from app.utils.response import APIResponse
from app.exceptions.custom_exceptions import DatabaseConnectionException

router = APIRouter(tags=["Health"], prefix="/health")

@router.get("/db")
def check_database():
    try:
        db = SessionLocal()
        db.execute(text("SELECT 1"))
        return APIResponse(status="ok", message="Conexión a la base de datos exitosa")
    except SQLAlchemyError as e:
        raise DatabaseConnectionException() from e
    finally:
        db.close()
