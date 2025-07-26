from fastapi import APIRouter
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from app.db.session import SessionLocal

router = APIRouter(tags=["Health"], prefix="/health")

@router.get("/db")
def check_database():
    try:
        db = SessionLocal()
        db.execute(text("SELECT 1"))
        return {"status": "ok", "message": "Conexión a la base de datos exitosa"}
    except SQLAlchemyError as e:
        return {"status": "error", "message": str(e)}
    finally:
        db.close()
