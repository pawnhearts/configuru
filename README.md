Usage example:

create if your project some file like settings.py:

from configuru import Config

class Config(Config):
    db_url:str = 'postgres://user:pass@postgres/postgres'

config = Config()

It must include type annotations! They are used to convert environment variables.

to use it:

from myapp.settings import config

print(config.db_url)

it would check for .env file and environment variable DB_URL
