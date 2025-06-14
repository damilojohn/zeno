from sqlalchemy import create_engine, Engine, text
from sqlalchemy.orm import sessionmaker, Session

from zeno.api.models.base import Base
from zeno.api.core.config import Settings
from typing import TypeAlias
from collections.abc import AsyncGenerator
import structlog

from fastapi import Request

LOG = structlog.stdlib.get_logger()


# Factory functions for creating db engine and session
def _create_engine(conn_string: str):
    return create_engine(conn_string)


def create_session(engine: Engine):
    return sessionmaker(autocommit=False, autoflush=False, bind=engine)


SessionMaker: TypeAlias = sessionmaker[Session]


# dependencies for getting db session
async def get_db_session(
        request: Request,
) -> AsyncGenerator[Session]:
    session_maker = request.app.state.session_maker
    session: Session = session_maker()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()


def create_tables_dev(engine: Engine):
    try:
        # LOG.info("🔄 Dropping all tables...")
        # Base.metadata.drop_all(bind=engine)
        LOG.info("🔄 Creating all tables...")
        Base.metadata.create_all(bind=engine)
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
            conn.execute(text('CREATE EXTENSION IF NOT EXISTS vector'))
            conn.commit()
        create_tables_dev(engine)
        LOG.info("Successfully Setup up DB tables......")
    if settings.is_production:
        LOG.info("Production env: Use Alembic migrations")
        check_alembic_current(engine)
