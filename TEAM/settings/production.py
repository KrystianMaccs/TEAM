from .base import *
from decouple import config

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config("DATABASE_NAME"),
        'USER': config("DATABASE_USER"),
        'PASSWORD': config("DATABASE_PASSWORD"),
        'HOST': config("DATABASE_HOST"),
        'PORT': config("DATABASE_PORT"),
    }
}

# Email Settings
"""EMAIL_USE_TLS: 
EMAIL_HOST: 
EMAIL_HOST_USER: config()
EMAIL_HOST_PASSWORD: config()
EMAIL_PORT: 
EMAIL_BACKEND:"""