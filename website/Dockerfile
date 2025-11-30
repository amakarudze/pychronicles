FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive
WORKDIR /website

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3.12 python3.12-venv python3-pip build-essential libpq-dev postgresql-client git curl libffi-dev libssl-dev netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

RUN python3.12 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN pip install --upgrade pip setuptools wheel
RUN pip install poetry==2.2.1

COPY pyproject.toml poetry.lock* ./
RUN poetry install --without dev --no-root

COPY . .

COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

EXPOSE 8000
ENTRYPOINT ["./entrypoint.sh"]
