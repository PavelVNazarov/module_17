# Домашнее задание по модулю 17
# Назаров ПВ

import logging

from fastapi import FastAPI
from .backend.db import engine
from .models import Base
#from .backend.db import Base

# Настройка логирования
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

app = FastAPI()

# Создаем все таблицы в базе данных
Base.metadata.create_all(bind=engine)

@app.get('/')
def read_root():
    return {"message": "Welcome to Taskmanager"}

