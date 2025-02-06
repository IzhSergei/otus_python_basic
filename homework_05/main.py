import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from app import router as api_router

app=FastAPI()

templates = Jinja2Templates(directory="templates")

"""Роуты для обычных представлений"""
@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/about/")
def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

"""Подключение API роутера"""
app.include_router(api_router)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
