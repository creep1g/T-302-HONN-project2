# syntax=docker/dockerfile:1

FROM postgres

ENV POSTGRES_USER "postgres"
ENV POSTGRES_PASSWORD "password"
ENV POSTGRES_DB "inventory"

EXPOSE 5432

COPY inventory.sql /docker-entrypoint-initdb.d/
