"""
Django settings for benovate project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""
import environ

# Django environ
root = environ.Path(__file__) - 2
env = environ.Env(
    DEBUG=(bool, True),
    SECRET_KEY=(str, '*4ysmox*olgcbauzt*2*o60p4gf2bb-c2afh!qu@q5g70(3bk8'),
    DATABASE_URL=(str, 'psql://postgres:postgres@localhost/postgres')
)

environ.Env.read_env(env_file=root('.env'))

# Build paths inside the project like this: root('path/subdir')
BASE_DIR = root()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = ['*']   # XXX


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'bootstrap4',

    'users',
    'txs',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'benovate.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            root('templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'builtins': [
                'django.templatetags.i18n',
                'bootstrap4.templatetags.bootstrap4',
            ],
        },
    },
]

WSGI_APPLICATION = 'benovate.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {'default': env.db()}
DATABASES['default']['CONN_MAX_AGE'] = 500


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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


# Custom user model
# https://docs.djangoproject.com/en/2.0/topics/auth/customizing

AUTH_USER_MODEL = 'users.User'


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (root('static'),)

# Fixtures
# https://docs.djangoproject.com/en/2.2/howto/initial-data/

FIXTURE_DIRS = (root('fixtures'),)
