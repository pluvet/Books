FROM python:3.8.13-alpine

RUN mkdir -p /app

RUN apk add curl
RUN apk add bash
# Install Poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
        ln -s /opt/poetry/bin/poetry && \
            poetry config virtualenvs.create false

# Copy poetry.lock* in case it doesn't exist in the repo
COPY ./pyproject.toml ./poetry.lock* /app/

WORKDIR /app/

RUN mkdir -p /source

RUN poetry install --no-root

RUN pip install psycopg2-binary

COPY ./source /app/source


