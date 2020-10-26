from config import config

import os
print('env DBURL:', os.environ.get('DB_URL'))
print('config:', config.db_url)

