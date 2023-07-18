FROM python:3.10-slim as build

ENV PIP_DEFAULT_TIMEOUT=100 \
    # Allow statements and log messages to immediately appear
    PYTHONUNBUFFERED=1 \
    # disable a pip version check to reduce run-time & log-spam
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    # cache is useless in docker image, so disable to reduce image size
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.5.0

WORKDIR /app
COPY ./pyproject.toml ./poetry.lock ./

RUN pip install "poetry==$POETRY_VERSION" \
    && poetry export -f requirements.txt -o requirements.txt --only web


### Final stage
FROM python:3.10-slim as final

WORKDIR /app

COPY --from=build /app/requirements.txt .

RUN set -ex \
    # Create a non-root user
    && addgroup --system --gid 1001 appgroup \
    && adduser --system --uid 1001 --gid 1001 --no-create-home appuser \
    # Upgrade the package index and install security upgrades
    && apt-get update \
    && apt-get upgrade -y \
    # Install dependencies
    && pip install -r requirements.txt \
    # Clean up
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

COPY ./templates/ templates/
COPY variante.py variante.py
COPY thompson_agent.py thompson_agent.py
COPY app.py app.py
COPY ./infra/ infra/

EXPOSE 5000

ENTRYPOINT ["python", "app.py"]