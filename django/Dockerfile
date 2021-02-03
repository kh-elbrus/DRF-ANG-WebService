FROM python:3.8-alpine 

LABEL MAINTAINER khalmukhamedov.e@gmail.com

ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev 
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

RUN mkdir /backend-app
WORKDIR /backend-app
COPY ./backend-app /backend-app

RUN mkdir -p /rsc/web/media
RUN mkdir -p /rsc/web/static
RUN adduser -D drfa-user
RUN chown -Rdrfa-user:drfa-user /rsc/
RUN chmod 755 /rsc/web 
USER drfa-user
