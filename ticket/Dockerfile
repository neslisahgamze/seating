# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt --no-cache-dir
COPY . /code/

# # [Security] Limit the scope of user who run the docker image
# RUN adduser -D user

# USER user
