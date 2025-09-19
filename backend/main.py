from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Разрешаем CORS — чтобы сайт мог обращаться к API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
        "text": "Ты — молодец! Твой сайт теперь умеет общаться с сервером 😊"
    }