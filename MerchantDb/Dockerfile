# syntax=docker/dockerfile:1

FROM postgres

ENV POSTGRES_USER "postgres"
ENV POSTGRES_PASSWORD "password"
ENV POSTGRES_DB "merchants"

EXPOSE 5432

COPY merchants.sql /docker-entrypoint-initdb.d/
