from fastapi import APIRouter, Depends
from app.utils.response import APIResponse
from app.exceptions.custom_exceptions import NotFoundException
from app.crud import user as user_crud
from sqlalchemy.orm import Session
from app.db.session import get_db
# Crear un router para las rutas de usuarios
router = APIRouter(tags=["Users"], prefix="/users")
# Endpoint para obtener todos los usuarios
@router.get("/")
def get_users(db: Session = Depends(get_db), response_model = APIResponse):
    users = user_crud.get_all_users(db=db)
    return APIResponse(status="success", message="Usuarios encontrados", data=users)
# Endpoint para obtener un usuario por ID
# @router.get("/{user_id}")
# def get_user(user_id: int, db: Session = Depends(get_db), response_model = APIResponse):
#     user = get_user_by_id(user_id, db)
#     if not user:
#         raise NotFoundException(name="Usuario")
#     return APIResponse(status="success", message="Usuario encontrado", data=user)
# # Endpoint para registrar un nuevo usuario
# @router.post("/register")
# def register_user(data: UserCreate, db: Session = Depends(get_db), response_model = APIResponse):
#     new_user = create_user(data, db)
#     return APIResponse(status="success", message="Usuario registrado", data=new_user)