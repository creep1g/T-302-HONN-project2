from enum import Enum
from pydantic import (BaseSettings)

class ContainerSettingEnum(Enum):
    def get(self, *argv):
        return self.value


class Environment(ContainerSettingEnum):
    PROD = 'prod'


class Settings(BaseSettings):
    postsgres_log_host: str
    postgres_log_database: str
    postgres_log_user: str
    postgres_log_password: str

    environment: Environment

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
