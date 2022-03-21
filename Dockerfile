FROM python:3.8

ENV DockerHOME=/app

WORKDIR $DockerHOME

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . $DockerHOME

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 8000