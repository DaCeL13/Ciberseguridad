from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hola Daniel Castellanos, tu API 'main.py' está viva"}
