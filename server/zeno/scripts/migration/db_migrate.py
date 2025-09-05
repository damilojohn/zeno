from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
import sys
import os

# Add your project to Python path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from zeno.api.core.config import Settings
from zeno.api.models.base import Base

# Global settings
settings = Settings

# Alembic Config object
config = context.config

# Set database URL from your settings
config.set_main_option("sqlalchemy.url", settings.database_url)

# Set up logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata


def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    # run_migrations_offline()
    pass
else:
    run_migrations_online()
