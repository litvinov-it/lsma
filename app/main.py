# Imports
# Из папки импортируем весь файл models (как класс, библиотека)
from . import models
from .routes import post
from fastapi import FastAPI
from .database import engine

# Init FastAPI app
app = FastAPI()

# Создает все имеющиеся таблицы. Если уже есть - пропускает
models.Base.metadata.create_all(bind=engine)

# Create home endpoint
@app.get('/')
def root():
    return {'status': 200, 'message': 'server working'}

# Init endpoint for post
app.include_router(post.router)