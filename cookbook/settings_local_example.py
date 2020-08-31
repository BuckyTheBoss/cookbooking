import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SPOONACULAR_API = 'api-key'
SECRET_KEY = 'secret-key'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

TIME_ZONE = 'Israel'
