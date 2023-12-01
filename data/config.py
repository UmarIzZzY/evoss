from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
# BOT_TOKEN = env.str("6146304144:AAGRgRAe8Eghs2UALhM-W8ERr_E-ZsRpZBg")  # Bot toekn
# ADMINS = env.list([364603275])  # adminlar ro'yxati
# IP = env.str("ip")  # Xosting ip manzili

BOT_TOKEN = '6146304144:AAGRgRAe8Eghs2UALhM-W8ERr_E-ZsRpZBg'
ADMINS = [364603275]

DATABASE = {
    'NAME': 'evos_bot',
    'USER': 'postgres',
    'PASSWORD': 'postgres',
    'HOST': 'localhost',
    'PORT': '5432',
}

