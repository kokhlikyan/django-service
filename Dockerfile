FROM python:3.9-alpine3.16

RUN apk update && apk add --no-cache \
    gcc \
    python3-dev \
    musl-dev \
    postgresql-dev \
    postgresql-client \
    build-base

COPY ./requirements.txt /temp/requirements.txt
COPY service /

WORKDIR /service

EXPOSE 8000

RUN pip install --upgrade pip
RUN pip install -r /temp/requirements.txt

RUN adduser -D service-user
USER service-user