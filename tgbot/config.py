from pydantic_settings import BaseSettings


class Config(BaseSettings):
    bot_token: str
    mongo_user: str = ''
    mongo_password: str = ''

    @property
    def db_url(self):
        return (f'mongodb://{self.mongo_user}:{self.mongo_password}'
                f'@localhost:27017/')
