from pydantic import BaseModel


class EmailConfig(BaseModel):
    username: str
    password: str
