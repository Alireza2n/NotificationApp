from decouple import config

CELERY_BROKER_URL = config('CELERY_BROKER_URL', default='pyamqp://guest@localhost:56708//')
CELERY_BACKEND_URL = config('CELERY_BACKEND_URL', default='redis://localhost:63720/0/')
CACHE_BACKEND_URL = config('CACHE_BACKEND_URL', default='redis://localhost:63720/1/')

TELEGRAM_TOKEN = config('TELEGRAM_TOKEN', default='')
