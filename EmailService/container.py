from dependency_injector import containers, providers

from email_config import EmailConfig
from Settings import Settings
from email_handler import EmailHandler


class Container(containers.DeclarativeContainer):
    config: Settings = providers.Configuration()

    __email_config = providers.Singleton(EmailConfig,
                                         username=config.email_username,
                                         password=config.email_password)

    email_handler_provider = providers.Singleton(
        EmailHandler,
        __email_config
    )
