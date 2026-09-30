from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API operacional"}

# Para rodar o código : uvicorn main:app --reload