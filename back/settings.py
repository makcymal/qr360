import os, sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(PROJECT_DIR)

# api app dir
sys.path.insert(0, PROJECT_DIR)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = os.environ.get('SECRET_KEY')
SECRET_KEY = 'django-insecure-v%n%urhg#$3i9ofm-6-6_dgy@r=sk^dnz2fft(=$nc0x+-usl1'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = int(os.environ.get('DEBUG', default=0))
DEBUG = True

# Our production host, this or 'qr360.tk/' or any else
PROD_HOST = 'kchaw.ru/'

# ALLOWED_HOSTS = []
# if os.environ.get('DJANGO_ALLOWED_HOSTS') is not None:
#     ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS').split(' ')
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'back.api',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'back.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['front/dist'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'back.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# DATABASES = {
#     "default": {
#         "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
#         "NAME": os.environ.get("SQL_DATABASE", os.path.join(BASE_DIR, "db.sqlite3")),
#         "USER": os.environ.get("SQL_USER", "user"),
#         "PASSWORD": os.environ.get("SQL_PASSWORD", "password"),
#         "HOST": os.environ.get("SQL_HOST", "localhost"),
#         "PORT": os.environ.get("SQL_PORT", "5432"),
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Asia/Vladivostok'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

MIDDLEWARE_CLASSES = (
    'whitenoise.middleware.WhiteNoiseMiddleware',
)

STATIC_URL = 'static/'

# Place static in the same location as webpack build files
STATIC_ROOT = os.path.join(BASE_DIR, 'front', 'dist', 'static')
STATICFILES_DIRS = []
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Saving images on server
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


REST_FRAMEWORK = {
    # API responses renderers   
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        # disable in prod
        'rest_framework.renderers.BrowsableAPIRenderer',
    ]
}


# access to API from different source
CORS_ALLOWED_ORIGINS = [
    # vue dev server
    'http://0.0.0.0:8000',
    'http://localhost:3000',
    'http://localhost:8000',
    'http://localhost:8080',
    'http://kchaw.ru',
    'https://kchaw.ru',
    'http://qr360.tk',
    'https://qr360.tk',
]


# CELERY_BROKER_URL = os.environ.get('CELERY_BROKER')
# CELERY_RESULT_BACKEND = os.environ.get('CELERY_BACKEND')
CELERY_BROKER_URL = "redis://redis:6379"
CELERY_RESULT_BACKEND = "redis://redis:6379"


# telegram bot secret key for auth
TGBOT = '5195521399:AAHCKGLCVmrQ19xQ5g6hSL5SqPQfXQvSbpg'
