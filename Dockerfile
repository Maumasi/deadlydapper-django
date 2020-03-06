FROM python:3.7-alpine
MAINTAINER Maumasi Consulting

ENV PYTHONUNBUFFERED=1

# RUN adduser -D maumasi
# USER maumasi
WORKDIR /var/www/deadlydapper

COPY ./requirements.txt /requirements.txt

RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .temp-build-deps \
            gcc libc-dev linux-headers postgresql-dev

RUN pip install -r /requirements.txt
# remove temp dependancies
RUN apk del .temp-build-deps


COPY ./app ./

