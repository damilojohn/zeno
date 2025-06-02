from typing import TypedDict
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

import structlog

from zeno.api.core.db import (_create_engine,
                              create_session,
                              Engine,
                              SessionMaker,
                              )

from zeno.api.core.config import Settings
# from zeno.api.search.endpoints import router as search_router
from zeno.api.user.endpoints import router as user_router

LOG = structlog.get_logger()


class State(TypedDict):
    engine: Engine
    session: SessionMaker


def configure_cors(app: FastAPI, settings: Settings) -> None:
    app.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_origins=[settings.cors_origin],
        allow_methods=["*"],
        allow_headers=["*"],
    )

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[State]:
    LOG.info("Zeno API starting.....")

    # set up app state
    # load global settings

    settings = Settings()
    engine = _create_engine(settings.database_url)
    session_maker = create_session(engine)
    configure_cors(app, settings)

    try:
        LOG.info("Zeno API started.......")

        yield {
            "engine": engine,
            "session": session_maker
            }
    finally:
        engine.dispose()

    LOG.info("Zeno API shutting down.........")


def create_app() -> FastAPI:
    app = FastAPI(title="Zeno's Backend",
                  lifespan=lifespan)
    # Add exception handlers later

    # add routers
    # app.include_router(search_router)
    app.include_router(user_router)

    return app


app = create_app()

if __name__ == "__main__":
    LOG.info("server starting.....", host="0.0.0.0")
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        log_level="info",
        port=8000,
        reload=True
    )
