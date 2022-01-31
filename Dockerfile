FROM python:3.8

ENV PYTHONUNBUFFERED 1

# Project Files and Settings
RUN pip install --upgrade pip
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
COPY . /app
WORKDIR /app