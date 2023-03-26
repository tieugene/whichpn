from typing import Dict

DEBUG = False
ALLOWED_HOSTS=['*']
SECRET_KEY = 'supersecretkey'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/var/lib/whichpn/db.sqlite3',
    }
}
SPECIAL: Dict[str, int] = {'"ГУО(Гл.упp.охpаны)"': 1, 'Мин.Обороны': 2}
