from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Привет из Python API!"}

@app.get("/stats")
def get_stats():
    return {
        "users": 1234,
        "orders": 567,
        "revenue": "₽890 000"
    }

@app.get("/message")
def get_message():
    return {
        "text": "Ты — молодец! Твой сайт теперь умеет общаться с сервером сосалкиных😊"
    }