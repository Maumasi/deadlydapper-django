FROM python:3.7-alpine
MAINTAINER Maumasi Consulting

ENV PYTHONUNBUFFERED=1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /add
WORKDIR /app
COPY ./app /app

RUN adduser -D maumasi
USER maumasi

