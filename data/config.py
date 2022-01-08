from environs import Env

env = Env()
env.read_env()

TOKEN = env.str('TOKEN')
admins = env.list('ADMINS')
for i, elem in enumerate(admins):
    admins[i] = int(elem)
