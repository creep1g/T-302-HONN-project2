# syntax=docker/dockerfile:1

FROM postgres

ENV POSTGRES_USER "postgres"
ENV POSTGRES_PASSWORD "password"
ENV POSTGRES_DB "buyers"

EXPOSE 5432

COPY buyers.sql /docker-entrypoint-initdb.d/
