import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../app"))

import asyncio
from logging.config import fileConfig

from alembic import context
from sqlmodel import SQLModel

from app.core.config import settings
from app.core.database import engine
import app.models

config = context.config
fileConfig(str(config.config_file_name))

target_metadata = SQLModel.metadata


def run_migrations_offline():
    url = settings.DATABASE_URL
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection):
    context.configure(connection=connection, target_metadata=target_metadata)

    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online():
    async with engine.begin() as conn:
        await conn.run_sync(do_run_migrations)
    await engine.dispose()


if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())
