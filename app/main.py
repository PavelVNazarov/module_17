# Домашнее задание по модулю 17
# Назаров ПВ



from fastapi import FastAPI
from routers import task, users

app = FastAPI()

app.include_router(task.router)
app.include_router(users.router)

@app.get("/")
async def root():
    return {"message": "Welcome to Taskmanager"}