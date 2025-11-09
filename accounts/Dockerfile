FROM python:3.13-alpine3.22

RUN pip install poetry==2.2.1

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /accounts

COPY pyproject.toml .
RUN touch README.md

RUN poetry install --without dev --no-root && rm -rf $POETRY_CACHE_DIR

COPY . .

RUN poetry install --without dev --no-root

EXPOSE 8000

CMD ["gunicorn", "accounts.wsgi:application", "--bind", "0.0.0.0:8000"]