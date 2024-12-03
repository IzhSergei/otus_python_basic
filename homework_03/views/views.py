from fastapi import APIRouter
from fastapi import Request
from fastapi.templating import Jinja2Templates


api_router = APIRouter()

templates = Jinja2Templates(directory="templates")

@api_router.get("/")
def main_route(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request, "title": "Home"}
    )


@api_router.get("/about")
def main_route(request: Request):
    return templates.TemplateResponse(
        "about.html", {"request": request, "title": "about"}
    )


@api_router.get("/ping")
def get_pong():
    return {"message":"pong"}