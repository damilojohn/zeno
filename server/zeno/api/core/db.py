from typing import TypeAlias
from collections.abc import AsyncGenerator

from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine, Engine
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncEngine,
    async_sessionmaker,
    AsyncSession,
)
from sqlalchemy import text

from zeno.api.models.base import Base
from zeno.api.core.config import Settings
import structlog

from fastapi import Request

LOG = structlog.stdlib.get_logger()


# Factory functions for creating db engine and session
def _create_engine(conn_string: str):
    """Factory functions for creating db engine"""
    return create_engine(conn_string)


def _create_async_engine(conn_string: str):
    """Factory functions for creating async db engine"""
    return create_async_engine(
        conn_string,
        connect_args={"ssl": "require"},
        pool_size=5,
        max_overflow=10,
        pool_recycle=1800,
        pool_pre_ping=True,
    )


def create_session(engine: Engine):
    return sessionmaker(autocommit=False, autoflush=False, bind=engine)


def create_async_session(engine: AsyncEngine):
    return async_sessionmaker(autocommit=False, autoflush=False, bind=engine)


SessionMaker: TypeAlias = sessionmaker[Session]
AsyncSessionMaker: TypeAlias = async_sessionmaker[AsyncSession]


# dependencies for getting db session
async def get_db_session(
    request: Request,
) -> AsyncGenerator[Session]:
    """
    Dependency to get a synchronous db session
    """
    session_maker = request.app.state.session_maker
    session: Session = session_maker()
    try:
        yield session
        session.commit()
    except Exception as e:
        LOG.info(f"db session failed with exception {e}")
        session.rollback()
        raise e
    finally:
        session.close()


async def get_async_db_session(
    request: Request,
) -> AsyncGenerator[AsyncSession]:
    """
    Dependency to get an asynchronous db session
    """
    session_maker = request.app.state.session_maker
    async with session_maker() as session:
        try:
            yield session
            await session.commit()
        except Exception as e:
            LOG.info(f"db session failed with exception {e}")
            await session.rollback()
            raise e


def create_tables_dev(engine: Engine):
    """Instantiate all tables in the database"""
    try:
        # LOG.info("🔄 Dropping all tables...")
        # Base.metadata.drop_all(bind=engine)
        LOG.info("🔄 Creating all tables...")
        Base.metadata.create_all(bind=engine)
    except Exception as e:
        LOG.error(f"error creating tables: {e}")
        raise e


async def create_tables_dev_async(engine: AsyncEngine):
    """Instantiate all tables in the database using async engine"""
    try:
        # LOG.info("🔄 Dropping all tables...")
        # async with engine.begin() as conn:
        #     await conn.run_sync(Base.metadata.drop_all)
        LOG.info("🔄 Creating all tables...")
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
    except Exception as e:
        LOG.error(f"error creating tables: {e}")
        raise e


def check_alembic_current(engine: Engine):
    """Production: Check if migrations are up to date"""
    from alembic.config import Config
    from alembic.runtime.migration import MigrationContext
    from alembic.script import ScriptDirectory

    try:
        alembic_cfg = Config("alembic.ini")
        script = ScriptDirectory.from_config(alembic_cfg)

        with engine.connect() as connection:
            context = MigrationContext.configure(connection)
            current_rev = context.get_current_revision()
            head_rev = script.get_current_head()

            if current_rev != head_rev:
                LOG.info("⚠️  Database not up to date!")
                LOG.info(f"   Current: {current_rev}")
                LOG.info(f"   Latest:  {head_rev}")
                LOG.info("   Run: alembic upgrade head")
                return False
            else:
                LOG.info("✅ Database is up to date")
                return True
    except Exception as e:
        LOG.error(f"❌ Error checking migrations: {e}")
        return False


def init_db(engine: Engine, settings: Settings):
    """Initialize db tables"""
    if settings.is_development:
        LOG.info("setting up tables using create_all() ....")
        with engine.connect() as conn:
            # Create pgvector extension
            conn.execute(text("CREATE EXTENSION IF NOT EXISTS vector"))
            conn.commit()
        create_tables_dev(engine)
        LOG.info("Successfully Setup up DB tables......")
    if settings.is_production:
        LOG.info("Production env: Use Alembic migrations")
        check_alembic_current(engine)


async def init_db_async(engine: AsyncEngine, settings: Settings):
    """Initialize db tables using async engine"""

    if settings.is_development:
        LOG.info("Setting up tables using create_all()....")
        async with engine.begin() as conn:
            await conn.execute(text("CREATE EXTENSION IF NOT EXISTS vector"))
            await conn.commit()
        await create_tables_dev_async(engine)
        LOG.info("Successfully setup DB tables....")
    if settings.is_production:
        LOG.info("Production env: Use Alembic migrations")
        # check_alembic_current(engine)
