# Image
FROM python:3.9-alpine

# Fix cryptography
ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1

# OS
RUN apk add --update
RUN apk add build-base
RUN apk add \
        gcc \
        libressl-dev \
        libffi-dev \
        musl-dev \
        openssl-dev \
        python3-dev \
        postgresql-dev

# Project files
COPY ./app /app

# Project dependency
RUN pip install poetry

COPY poetry.lock ./poetry.lock
COPY pyproject.toml ./pyproject.toml

RUN poetry install

# Current directory
WORKDIR /app

# Port
EXPOSE 80

# Start server
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]