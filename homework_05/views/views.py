from fastapi import APIRouter
from fastapi import Request
from fastapi.templating import Jinja2Templates
from views.users.crud import CarStorage
from views.users.utils import max_id

router = APIRouter()

"""  - создайте api router, укажите префикс `/api`"""
api_router = APIRouter(prefix="/api")

templates = Jinja2Templates(directory="templates")


@router.get("/")
def main_route(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request, "title": "Home"}
    )


"""добавьте страницу `/about/`, добавьте туда текст, информацию о сайте и разработчике"""


@router.get("/about")
def main_route(request: Request):
    return templates.TemplateResponse(
        "about.html", {"request": request, "title": "about"}
    )


"""добавьте вложенный роутер для вашей сущности """

"""  - добавьте представление для чтения сущности"""


@api_router.get("/car")
def get_record(id: int):
    if id <= max_id():
        record = CarStorage.get_record(id - 1)
        return {"message": f"Данные по авто №: {id}:", "record": record}
    else:
        return {"message": "ошибка"}


"""  - добавьте представление для чтения списка сущностей """


@api_router.get("/cars")
def get_all_records():
    records = CarStorage.get_all_records()
    return {"message": "Все записи успешно считаны", "record": records}


"""  - добавьте представление для создания сущности"""


@api_router.post(
    "/add-record",
    summary="Добавление новой записи",
    description="Добавляет новую запись в переменную и возвращает обновленный список записей.",
)
def add_record(model: str, number: str, owner: str):
    record = CarStorage.add_record(model, number, owner)
    if "error" in record:
        return {"message": "Данные не прошли валидацию!", "record": record}
    return {"message": "Запись успешно добавлена!", "record": record}
