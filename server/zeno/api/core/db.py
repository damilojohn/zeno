from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker, Session
from typing import TypeAlias
from collections.abc import AsyncGenerator

from fastapi import Depends, Request


# Factory functions for creating db engine and session
def _create_engine(conn_string: str):
    return create_engine(conn_string)


def create_session(engine: Engine):
    return sessionmaker(auto_commit=False, auto_flush=False, bind=engine)


SessionMaker: TypeAlias = sessionmaker[Session]


# dependencies for getting db session
async def get_db_sessionmaker(
        request: Request) -> AsyncGenerator[SessionMaker]:
    session_maker = request.state.session
    yield session_maker


async def get_db_session(
        request: Request,
        session_maker: SessionMaker = Depends(get_db_sessionmaker)
) -> AsyncGenerator[Session]:
    with session_maker() as session:
        if session := request.state.getattr("session", None):
            yield session
        else:
            try:
                session = session_maker()
                yield session
            except Exception as e:
                await session.rollback()
                raise e
            finally:
                session.close()
