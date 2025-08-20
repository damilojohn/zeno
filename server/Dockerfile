#Multi-stage build
FROM python:3.13 AS builder

LABEL org.opencontainers.image.source=https://github.com/zeno
LABEL org.opencontainers.image.description="Zeno"
LABEL org.opencontainers.image.licenses=Apache-2.0

WORKDIR /usr/app/server

COPY pyproject.toml uv.lock /usr/app/server/


RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential libpq-dev

RUN pip install uv && \
    uv sync

COPY /zeno /usr/app/server/zeno

RUN apt-get autoremove -y build-essential && \
    rm -rf /var/lib/apt/lists/*

FROM python:3.13-slim

WORKDIR /usr/app/server

COPY --from=builder /usr/app/server/zeno/ /usr/app/server/zeno/
COPY --from=builder /usr/app/server/.venv /usr/app/server/.venv

ENV PATH="/usr/app/server/.venv/bin:$PATH"

EXPOSE 8080

CMD ["uvicorn", "zeno.app:app", "--host=0.0.0.0", "--port=8080", "--loop=uvloop"]
# CMD ["gunicorn", "zeno.app:app", "bind=0.0.0.0:8080", "-w=4","-k=uvicorn.workers.UvicornWorker"]

