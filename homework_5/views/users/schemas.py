from pydantic import BaseModel, Field
from typing import Annotated

"""создаём базовый класс для сущности автомобиль, с проверкой полей с помощью pydantic"""

class Car(BaseModel):
    model: Annotated[str, Field(default="default model",min_length=3, max_length=15)]
    number: Annotated[str, Field(pattern=r"^\w\d{3}\w{2}\d{2,3}$", description="Номер авто должен быть в формате б/ццц/бб/цц или б/ццц/бб/ццц")]
    owner: Annotated[str, Field(default="default owner", min_length=3, max_length=12)]

