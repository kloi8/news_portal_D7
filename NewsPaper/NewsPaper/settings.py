"""
Django settings for NewsPaper project.

Generated by 'django-admin startproject' using Django 5.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os
from pathlib import Path
import datetime

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-z5=d-*5jh$-e9kq+ixep*0k94dr=3fn!xhl@+f925o742ne0^#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

#добавить бэкенды аутентификации
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend', #встроенный бэкенд Django реализующий аутентификацию по username
    'allauth.account.auth_backends.AuthenticationBackend', #бэкенд аутентификации, предоставленный пакетом allauth
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'news.apps.NewsConfig',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'fpages',
    'django_filters',
    'accounts',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.yandex',
    'django_apscheduler'
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'allauth.account.middleware.AccountMiddleware'
]

ROOT_URLCONF = 'NewsPaper.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request', # в конфигурации шаблонов присутствует контекстный процессор
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]


WSGI_APPLICATION = 'NewsPaper.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

LOGIN_REDIRECT_URL = "/news"

# В файл настроек проекта мы внесём дополнительные параметры,
# в которых укажем обязательные и необязательные поля.
# Обязательность полей остаётся на усмотрение разработчика.
# В нашем случае мы укажем следующую комбинацию параметров:

ACCOUNT_EMAIL_REQUIRED = True # поле email является обязательным
ACCOUNT_UNIQUE_EMAIL = True # поле email является уникальным
ACCOUNT_USERNAME_REQUIRED = False # username необязательный
ACCOUNT_AUTHENTICATION_METHOD = 'email' #аутентификация будет происходить посредством электронной почты
ACCOUNT_EMAIL_VERIFICATION = 'mandatory' #верификация почты отсутствует
ACCOUNT_CONFIRM_EMAIL_ON_GET = True

ACCOUNT_FORMS = {"signup": "accounts.forms.CustomSignupForm"}

# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'yandex': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': 'db18c2fc88c54f45b8cd9104a703ae7a',
            'secret': '19dd29fb55ea422d8fd2400aa000509c',
            'key': ''
        }
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' #работа с протоколом отправки сообщений
EMAIL_HOST = 'smtp.yandex.ru' #хост почтового сервера
EMAIL_PORT = 465 #порт, на который почтовый сервер принимает письма
EMAIL_HOST_USER = "newspapertest1@yandex.ru" #логин пользователя почтового сервера
EMAIL_HOST_PASSWORD = "nhshiairwcnjalop" #пароль пользователя почтового сервера
EMAIL_USE_TLS = False #необходимость использования TLS
EMAIL_USE_SSL = True #необходимость использования SSL

DEFAULT_FROM_EMAIL = "newspapertest1@yandex.ru" #почтовый адрес отправителя по умолчанию.



SERVER_EMAIL = "newspapertest1@yandex.ru" #где будет содержаться адрес почты,
# от имени которой будет отправляться письмо при вызове mail_admins
# и mail_manager
ADMINS = ( #будет хранить список имён менеджеров и адресов их почтовых ящиков.
    ('Karina', 'shanny.90@mail.ru'),
    )



EMAIL_SUBJECT_PREFIX = "[NP update]" #Пока что так

SITE_URL = 'http://127.0.0.1:8000'



CELERY_BROKER_URL = 'redis://localhost:6379' #указывает на URL брокера сообщений (Redis). По умолчанию он находится на порту 6379.
CELERY_RESULT_BACKEND = 'redis://localhost:6379' #указывает на хранилище результатов выполнения задач.
CELERY_ACCEPT_CONTENT = ['application/json'] #допустимый формат данных.
CELERY_TASK_SERIALIZER = 'json' #метод сериализации задач.
CELERY_RESULT_SERIALIZER = 'json' # метод сериализации результатов.