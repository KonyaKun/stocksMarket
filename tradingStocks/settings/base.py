from settings.conf import *
import os
import sys

ROOT_URLCONF = 'urls.urls'
AUTH_USER_MODEL = 'auths.CustomUser'

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
) # содержит путь до нашего проекта, но не содержит сам проект
sys.path.append(BASE_DIR) # добавили проект в путь
sys.path.append(os.path.join(BASE_DIR,'apps')) # добавили приложения в путь


# Apps

DJANGO_AND_THIRD_PARTY_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'django_extensions',
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
]
# регистрируем приложения здесь

PROJECT_APPS = [
    'stocksmarket.apps.StocksmarketConfig',
    'auths.apps.AuthsConfig',
    'abstracts.apps.AbstractsConfig'
]

INSTALLED_APPS = DJANGO_AND_THIRD_PARTY_APPS + PROJECT_APPS

# Static / Media

STATIC_URL = '/static/' # 
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/tradingStocks/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# добавили медию и статик в проект

# Middleware / Templates / Validators
# когда поступает запрос все проходит по этому порядку 
# 1) Request Middlewares - Запрос промежуточного программного обеспечения
# 2) URL Router (URL Dispatcher) - Маршрутизация URL
# 3) Views - Отображения
# 4) Context Processors - Контекстные процессоры
# 5) Template Renderers - Рендер шаблонов
# 6) Response Middlewares - Промежуточное программное обеспечение ответа

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
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

# CORS

# CORS_ORIGIN_ALLOW_ALL = True

CORS_ORIGIN_WHITELIST = [
    'http://localhost:5500',
    'http://localhost:1234',
]


CORS_ALLOW_HEADERS = [
    "accept",
    "authorization",
    "content-type",
    "user-agent",
    "Access-Control-Allow-Origin",
]


CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "PATCH",
    "POST",
    "PUT",
]

# Localization

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Asia/Almaty'

USE_I18N = True
USE_L10N = True
USE_TZ = True