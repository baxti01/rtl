from pydantic_settings import BaseSettings


class Config(BaseSettings):
    bot_token: str = ''
    mongo_host: str = 'localhost'
    mongo_port: int = 27017
    mongo_initdb_root_username: str = ''
    mongo_initdb_root_password: str = ''

    @property
    def db_url(self):
        if self.mongo_initdb_root_username and self.mongo_initdb_root_password:
            return (f'mongodb://{self.mongo_initdb_root_username}:'
                    f'{self.mongo_initdb_root_password}'
                    f'@{self.mongo_host}:{self.mongo_port}/')

        return f'mongodb://{self.mongo_host}:{self.mongo_port}/'


config = Config(
    _env_file='.env',
    _env_file_encoding='UTF-8'
)
