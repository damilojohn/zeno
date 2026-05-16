from typing import TypedDict
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import HTTPException, RequestValidationError
import uvicorn

from zeno.api.core.db import (
    _create_async_engine,
    create_async_session,
    AsyncEngine,
    AsyncSessionMaker,
    init_db_async,
)
from zeno.api.core.utils import LOG
from zeno.api.core.config import Settings
from zeno.api.core.exceptions import (
    AppException,
    app_exception_handler,
    http_exception_handler,
    validation_exception_handler,
)

from zeno.api.search.endpoints import router as search_router
from zeno.api.user.endpoints import router as user_router
from zeno.api.billing.endpoints import router as billing_router


settings = Settings()


class State(TypedDict):
    engine: AsyncEngine
    async_session_maker: AsyncSessionMaker


def configure_cors(app: FastAPI, settings: Settings) -> None:
    app.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_origins=[settings.cors_origin],
        allow_methods=["*"],
        allow_headers=["*"],
    )


@asynccontextmanager
async def lifespan(
    app: FastAPI,
) -> AsyncIterator[State]:
    LOG.info("Zeno API starting.....")

    # set up app state and load global settings
    engine = _create_async_engine(settings.database_url)
    await init_db_async(engine, settings)
    session_maker = create_async_session(engine)
    app.state.session_maker = session_maker

    try:
        LOG.info("Zeno API started.......")

        yield {"engine": engine, "session_maker": session_maker}
    finally:
        await engine.dispose()

    LOG.info("Zeno API shutting down.........")
    LOG.info("Bye!!")


def create_app() -> FastAPI:
    app = FastAPI(title="Zeno's Backend", lifespan=lifespan)

    app.add_exception_handler(AppException, app_exception_handler)
    app.add_exception_handler(HTTPException, http_exception_handler)
    app.add_exception_handler(RequestValidationError, validation_exception_handler)

    configure_cors(app, settings)
    app.include_router(search_router)
    app.include_router(billing_router)
    app.include_router(user_router)

    return app


app = create_app()

if __name__ == "__main__":
    LOG.info("server starting... on {settings.host}:{settings.port}")
    uvicorn.run(
        "zeno.app:app",
        host=settings.host,
        log_level="info",
        port=settings.port,
        reload=True,
    )
