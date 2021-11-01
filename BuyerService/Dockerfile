# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app/buyer

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8001

CMD ["python", "main.py"]
