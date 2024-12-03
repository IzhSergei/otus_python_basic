#Для сборки контейнера используйте строку:
# docker build -t my_fastapi_app .

# Для запуска контейнера используйте строку:
# docker run -d -p 8000:8000 --name homework_03 my_fastapi_app

FROM python:3.12-slim-bookworm

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

EXPOSE 8000
