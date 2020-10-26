import sys
sys.path.append('..')
from configuru import Config

class Config(Config):
    db_url:str = 'postgres://user:pass@postgres/postgres'
    debug:bool = False
    workers:int = 1

config = Config()

