from dependency_injector import containers, providers

from dbConnections.db_config import DbConfig
from dbConnections.postgres_db_connection import PostgresDbConnection
from buyer_repository import BuyerRepository
from Settings import Settings


class Container(containers.DeclarativeContainer):
    config: Settings = providers.Configuration()

    __db_config = providers.Singleton(DbConfig,
                                      host=config.postgres_log_host,
                                      user=config.postgres_log_user,
                                      database=config.postgres_log_database,
                                      password=config.postgres_log_password)

    db_connection_provider = providers.Singleton(
        PostgresDbConnection,
        __db_config
    )

    buyer_repository_provider = providers.Singleton(
        BuyerRepository,
        db_connection_provider
    )
