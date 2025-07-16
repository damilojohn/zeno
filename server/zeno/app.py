from typing import TypedDict
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from zeno.api.core.db import (_create_engine,
                              create_session,
                              Engine,
                              SessionMaker,
                              init_db
                              )
from zeno.api.core.utils import LOG
from zeno.api.core.config import Settings
# from zeno.api.search.endpoints import router as search_router
from zeno.api.user.endpoints import router as user_router


settings = Settings()

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
async def lifespan(app: FastAPI,) -> AsyncIterator[State]:
    LOG.info("Zeno API starting.....")

    # set up app state and load global settings
    engine = _create_engine(settings.database_url)
    init_db(engine, settings)
    session_maker = create_session(engine)
    app.state.session_maker = session_maker

    try:
        LOG.info("Zeno API started.......")

        yield {
            "engine": engine,
            "session_maker": session_maker
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
    configure_cors(app, settings)
    app.include_router(user_router)

    return app


app = create_app()

if __name__ == "__main__":
    LOG.info("server starting.....", host=settings.host)
    uvicorn.run(
        "zeno.app:app",
        host=settings.host,
        log_level="info",
        port=settings.port,
        reload=True
    )
