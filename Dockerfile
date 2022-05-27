# syntax=docker/dockerfile:1
FROM python:3.10 
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev
# RUN pip install -r requirements.txt
COPY . /code/
# RUN useradd thiago && \
#     chown -R thiago:thiago /code/composeexample && \
#     chown -R thiago:thiago /code/manage.py && \
#     pip3 install psycopg2-binary
