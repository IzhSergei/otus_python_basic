from typing import List
from views.users.schemas import Car

"""В этом модуле утилитарные функции для работы с содержимым Гаража"""

Garage = [
    Car(model="fiat", number="f345rt18", owner="nik"),
    Car(model="ford", number="t456ry18", owner="myke"),
]


def read_all() -> List[Car]:
    return Garage


def read_one(id) -> Car:
    return Garage[id]


def add_rec(data: Car):
    """Функция для добавления элемента в список Garage"""
    global Garage
    return Garage.append(data)


def max_id() -> int:
    """Функция определения максимального кол-ва авто в гараже"""
    count = len(Garage) + 1
    print(count)
    return count
