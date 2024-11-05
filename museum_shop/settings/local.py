from decouple import config
DEBUG = config('DEBUG', cast=bool)
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'museum_shop',
        'USER': 'root',
        'PASSWORD': 'Bo977731030#',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}