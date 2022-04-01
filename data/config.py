# parsing data from .env
from environs import Env

env = Env()
env.read_env()

TOKEN = env.str('TOKEN')
ADMINS = env.list('ADMINS')
for i, elem in enumerate(ADMINS):
    ADMINS[i] = int(elem)

# paths
RINGS_PATH = 'img/rings_tb.jpeg'
RINGS_CHANGES_PATH = 'data/rings_changes.txt'
LINKS_PATH = 'data/links.json'
DATABASE_PATH = 'data/users.db'
WEBDRIVER_PATH = 'C:/Program Files (x86)/ChromeDriver/chromedriver.exe'
SCREEN_PATH = 'img/'
