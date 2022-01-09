# parsing data from .env
from environs import Env

env = Env()
env.read_env()

TOKEN = env.str('TOKEN')
ADMINS = env.list('ADMINS')
for i, elem in enumerate(ADMINS):
    ADMINS[i] = int(elem)

# webhook settings
WEBHOOK_PATH = ''
WEBHOOK_URL = env.str('WEBHOOK_URL')

# webserver settings
WEBAPP_HOST = env.str('WEBAPP_HOST')  # or ip
WEBAPP_PORT = env.int('WEBAPP_PORT')
