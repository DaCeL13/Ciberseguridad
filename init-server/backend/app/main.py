from fastapi import FastAPI, Form
from app.db.base import Base
from app.db.session import engine
from fastapi.middleware.cors import CORSMiddleware

# Crear la instancia de FastAPI
app = FastAPI()

# Configurar CORS para permitir solicitudes desde el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost"],  # Permitir todas las orígenes
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register exception handlers

# Create tables
Base.metadata.create_all(bind=engine)


# Modelo de datos de Pydantic para la validación de la API
# class UserBase(BaseModel):
#     username: str
#     password: str

# class UserCreate(UserBase):
#     pass

# class User(UserBase):
#     id: int
#     class Config:
#         orm_mode = True

# # Modelo de datos de SQLAlchemy para la tabla de la base de datos
# class DBUser(Base):
#     __tablename__ = "users"
#     id = Column(Integer, primary_key=True, index=True)
#     username = Column(String(50))
#     password = Column(String(255))

# # Crea la tabla en la base de datos si no existe
# Base.metadata.create_all(bind=engine)


@app.get("/")
def read_root():
    return {"message": "Hola Daniel Castellanos, tu API 'main.py' está viva"}

@app.post("/login")
def login(username: str = Form(...), password: str = Form(...)):
    # if username == "admin" and password == "secret":
    return {"success": True, "message": "Login successful"}
    # return {"message": "Invalid credentials"}, 401

# @app.get("/test-conexion")
# def test_connection(db: Session = Depends(get_db)):
#     """
#     Endpoint para probar la conexión a la base de datos.
#     """
#     try:
#         # Intenta ejecutar una consulta simple para verificar la conexión
#         db.execute("SELECT 1")
#         return {"message": "Conexión a la base de datos exitosa."}
#     except Exception as e:
#         raise HTTPException(
#             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#             detail=f"Error al conectar a la base de datos: {e}"
#         )

