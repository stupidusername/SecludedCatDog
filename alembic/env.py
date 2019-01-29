from pathlib import Path
import sys

# Add the parent folder path to the sys.path list.
sys.path.append(str(Path(__file__).resolve().parents[1]))
print(sys.path)

from alembic import context
from config import Config
from logging.config import fileConfig
from sqlalchemy import create_engine, pool

# App Config object.
config = Config()

# Interpret the alembic config file for Python logging.
# This line sets up loggers basically.
fileConfig(context.config.config_file_name)


def run_migrations_offline():
    """
    Run migrations in 'offline' mode.

    This configures the context with just a URL and not an Engine, though an
    Engine is acceptable here as well. By skipping the Engine creation we don't
    even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the script output.
    """
    context.configure(config.get_sql_alchemy_url(), literal_binds=True)

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """
    Run migrations in 'online' mode.

    In this scenario we need to create an Engine and associate a connection
    with the context.
    """
    connectable = create_engine(
        config.get_sql_alchemy_url(),
        poolclass=pool.NullPool)

    with connectable.connect() as connection:
        context.configure(connection=connection)
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
