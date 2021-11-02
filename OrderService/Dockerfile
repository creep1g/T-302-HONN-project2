# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app/orders

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "main.py"]
