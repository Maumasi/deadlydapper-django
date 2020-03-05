FROM python:3.7-alpine
MAINTAINER Maumasi Consulting

ENV PYTHONUNBUFFERED=1

# RUN adduser -D maumasi
# USER maumasi
WORKDIR /var/www/deadlydapper

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# RUN mkdir /app

COPY ./app ./

