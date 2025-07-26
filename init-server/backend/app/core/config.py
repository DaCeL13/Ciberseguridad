import os
from dotenv import load_dotenv
from urllib.parse import quote_plus

# Carga las variables de entorno
load_dotenv()

class Settings:
    # Extraemos cada parte de la URL de forma segura
    DB_USER: str = os.getenv("DB_USER")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD")
    DB_HOST: str = os.getenv("DB_HOST")
    DB_PORT: str = os.getenv("DB_PORT")
    DB_NAME: str = os.getenv("DB_NAME")

    # Codificamos la contraseña para evitar errores con caracteres especiales
    encoded_password = quote_plus(DB_PASSWORD)

    # Construimos la URL completa para SQLAlchemy
    DATABASE_URL = f"mysql+pymysql://{DB_USER}:{encoded_password}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Crea una instancia de la clase Settings
settings = Settings()