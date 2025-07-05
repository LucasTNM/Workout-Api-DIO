import asyncio
from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context
from workout_api.contrib.models import BaseModel

# Importar todos os modelos para que o Alembic os detecte
from workout_api.atleta.models import AtletaModel
from workout_api.categorias.models import CategoriaModel  
from workout_api.centro_treinamento.models import CentroTreinamentoModel

config = context.config


if config.config_file_name is not None:
    fileConfig(config.config_file_name)


target_metadata = BaseModel.metadata


def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()