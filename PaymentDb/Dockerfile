# syntax=docker/dockerfile:1

FROM postgres

ENV POSTGRES_USER "postgres"
ENV POSTGRES_PASSWORD "password"
ENV POSTGRES_DB "payments"

EXPOSE 5432

COPY payments.sql /docker-entrypoint-initdb.d/
