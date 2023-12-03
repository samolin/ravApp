FROM python:3.11.0

WORKDIR /app

COPY ./poetry.lock .
COPY ./pyproject.toml .
RUN mkdir downloads

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

COPY ./ravApp /app/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
