# parsing data from .env
from environs import Env

env = Env()
env.read_env()

TOKEN = env.str('TOKEN')
ADMINS = env.list('ADMINS')
for i, elem in enumerate(ADMINS):
    ADMINS[i] = int(elem)
