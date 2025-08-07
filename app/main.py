from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routers import home

app = FastAPI()

# Подключаем папку static для статики (CSS, картинки и т.д.)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(home.router)