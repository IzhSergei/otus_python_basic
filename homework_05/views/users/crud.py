from views.users.schemas import Car
from views.users.utils import read_all, read_one, add_rec
from pydantic import ValidationError

""" Методы для создания, чтения, добавления, удаления автомобилей из гаража """


class CarStorage:

    @staticmethod
    def validation(record):
        Car(**record)

    @staticmethod
    def get_record(id):
        return read_one(id)

    @staticmethod
    def get_all_records():
        return read_all()

    @staticmethod
    def add_record(model: str, number: str, owner: str):
        # Валидация данных
        try:
            new_car = Car(model=model, number=number, owner=owner)
            add_rec(new_car)
            return new_car
        except ValidationError as e:
            return {"error": e.errors()}
