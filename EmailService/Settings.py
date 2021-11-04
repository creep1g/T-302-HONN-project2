from enum import Enum
from pydantic import (BaseSettings)


class ContainerSettingEnum(Enum):
    def get(self, *argv):
        return self.value


class Settings(BaseSettings):
    email_username: str
    email_password: str

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
