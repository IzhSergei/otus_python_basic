"""
Домашнее задание №5
Первое веб-приложение

- в модуле `app` создайте базовое FastAPI приложение
- создайте обычные представления
  - создайте index view `/`
  - добавьте страницу `/about/`, добавьте туда текст, информацию о сайте и разработчике
  - создайте базовый шаблон (используйте https://getbootstrap.com/docs/5.0/getting-started/introduction/#starter-template)
  - в базовый шаблон подключите статику Bootstrap 5 (подключите стили), примените стили Bootstrap
  - в базовый шаблон добавьте навигационную панель `nav` (https://getbootstrap.com/docs/5.0/components/navbar/)
  - в навигационную панель добавьте ссылки на главную страницу `/` и на страницу `/about/` при помощи `url_for`
  - добавьте новые зависимости в файл `requirements.txt` в корне проекта
    (лучше вручную, но можно командой `pip freeze > requirements.txt`, тогда обязательно проверьте, что туда попало, и удалите лишнее)
- создайте api представления:
  - создайте api router, укажите префикс `/api`
  - добавьте вложенный роутер для вашей сущности (если не можете придумать тип сущности, рассмотрите варианты: товар, книга, автомобиль)
  - добавьте представление для чтения списка сущностей
  - добавьте представление для чтения сущности
  - добавьте представление для создания сущности
"""

import uvicorn
from fastapi import FastAPI
from views.views import router, api_router
from fastapi.staticfiles import StaticFiles

app=FastAPI()
app.include_router(router)
app.include_router(api_router)
app.mount("/static", StaticFiles(directory="static"), name="static")


if __name__ == '__main__':
    uvicorn.run("app:app", reload=True)

