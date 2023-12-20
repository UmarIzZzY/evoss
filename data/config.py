from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

BOT_TOKEN = '5985874761:AAFNRocf0s60Y1rfC3az-slCt5RfyDLjAYk'
ADMINS = [876439642]

DATABASE = {
    'NAME': 'evos_bot',
    'USER': 'postgres',
    'PASSWORD': 'UK101010',
    'HOST': 'localhost',
    'PORT': '5432',
}

