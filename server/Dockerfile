FROM python:3.13-slim as builder

LABEL org.opencontainers.image.source=https://github.com/zeno
LABEL org.opencontainers.image.description="Zeno"
LABEL org.opencontainers.image.licenses=Apache-2.0

RUN useradd -m appuser
USER appuser

WORKDIR /app/server/

# COPY pyproject.toml uv.lock /app/server/
RUN pip install uv
#copy source code
COPY /zeno/ /app/server/zeno
COPY pyproject.toml /app/server/pyproject.toml
COPY uv.lock /app/server/uv.lock
# RUN pip install uv

# Setup system dependencies
RUN apt-get update && \
    apt-get install  -y --no-install-recommends \ 
    build-essential libpq-dev \ 
    && uv sync --no-group \ 
    && apt-get autoremove -y build-essential\
    && rm -rf /var/lib/apt/lists/*

# FROM python:3.13-slim

# WORKDIR /app

# #get python dependencies
# COPY --from=builder /app/server/.venv/ /app/.venv/
ENV PATH="/app/server/.venv/bin:$PATH"
# #get source code
# COPY --from=builder /app/server/zeno /app/zeno


# RUN useradd -m appuser
# USER appuser


EXPOSE 8080
# CMD ["uvicorn","zeno.app:app","--port=8080"]
CMD ["uv","run" ,"task", "api"]
