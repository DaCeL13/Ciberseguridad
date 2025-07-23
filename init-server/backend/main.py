from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas las orígenes
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Hola Daniel Castellanos, tu API 'main.py' está viva"}

@app.post("/login")
def login(username: str = Form(...), password: str = Form(...)):
    # if username == "admin" and password == "secret":
    return {"success": True, "message": "Login successful"}
    # return {"message": "Invalid credentials"}, 401
