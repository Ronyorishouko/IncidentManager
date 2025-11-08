from .base import *
import os
from dotenv import load_dotenv

load_dotenv('/Imanager/.env')
SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = os.getenv('DEBUG')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('HOST'),
        'PORT': os.getenv('PORT'),
    }
}

