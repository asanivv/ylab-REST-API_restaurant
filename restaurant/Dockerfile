FROM python:3.10-slim

WORKDIR /home/restaurant

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /home/restaurant
RUN pip install --upgrade pip && python -m pip install -r requirements.txt

COPY . /home/restaurant