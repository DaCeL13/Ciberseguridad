from fastapi import FastAPI, APIRouter, Form
from app.db.base import Base
from app.db.session import engine
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.routes import health
from app.exceptions.custom_exceptions import NotFoundException, DatabaseConnectionException
from app.exceptions.handlers import not_found_exception_handler, db_connection_exception_handler

tags_metadata = [
    {
        "name": "Health",
        "description": "Endpoints para verificar el estado del sistema y la base de datos",
    },
    {
        "name": "Users",
        "description": "Operaciones relacionadas con usuarios: registro, login, perfil",
    },
]
# Crear la instancia de FastAPI
app = FastAPI(title="Initial Server API", version="1.0.0", openapi_tags=tags_metadata)

app.add_exception_handler(DatabaseConnectionException, db_connection_exception_handler)
app.add_exception_handler(NotFoundException, not_found_exception_handler)
# Crear un router para las rutas de la API
v1_router = APIRouter(prefix="/api/v1")
v1_router.include_router(health.router)

# Registrar el router health en la aplicación principal
app.include_router(v1_router)

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

