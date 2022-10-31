from .base import *
from decouple import config

EMAIL_USE_TLS=True
EMAIL_HOST: config("EMAIL_HOST")
EMAIL_HOST_USER: config("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD: config("EMAIL_HOST_PASSWORD")
EMAIL_PORT: 587
EMAIL_BACKEND: config("EMAIL_BACKEND")


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}