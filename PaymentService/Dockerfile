# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app/payments

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5672

CMD ["python", "main.py"]
