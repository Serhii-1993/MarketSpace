"""
Django settings for marketSpace project.

Generated by 'django-admin startproject' using Django 5.0.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os

import categories.apps
import comments.apps
import favorites.apps
import products.apps
import user_auth.apps
import users.apps

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-pn2u(8&p4l0vjxmpe8ylj2-asw^_t1^54x1cxg0cy7zv(_y!nd'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*',]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # APPS:
    'rest_framework',
    'mptt',  # django-mptt for categories hierarchy
    'users.apps.UsersConfig',
    'products.apps.ProductsConfig',
    'comments.apps.CommentsConfig',
    'user_auth.apps.UserAuthConfig',
    'categories.apps.CategoriesConfig',
    'favorites.apps.FavoritesConfig',
    'search.apps.SearchConfig',

    'corsheaders',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'allauth.socialaccount.providers.google',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # ADD:
    "allauth.account.middleware.AccountMiddleware",
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'marketSpace.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # ADD:
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'marketSpace.wsgi.application'

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
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.Users'

AUTHENTICATION_BACKENDS = [

    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',

]

# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': '855166978277-edau1sndkpvjvnmmlilj7fj31opji0vu.apps.googleusercontent.com',
            'secret': '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',
            'key': ''
        }
    }
}

# URL, на який буде перенаправлено після успішного входу користувача
LOGIN_REDIRECT_URL = '/api/prod/'

# URL-адреса для входу (вказується для допомоги підсистемі автентифікації)
# ACCOUNT_LOGIN_URL = '/accounts/login/'

# URL, на який буде перенаправлено після виходу з облікового запису
# ACCOUNT_LOGOUT_REDIRECT_URL = '/'

# URL для сторінки реєстрації
# ACCOUNT_SIGNUP_URL = '/accounts/signup/'

# URL, на який буде перенаправлено після успішної реєстрації
# ACCOUNT_SIGNUP_REDIRECT_URL = '/'

ACCOUNT_ADAPTER = 'users.adapter.MyAccountAdapter'

CORS_ALLOW_ALL_ORIGINS = True

CSRF_TRUSTED_ORIGINS = [
    'https://thirty-cases-wink.loca.lt',
    'https://odd-deer-joke.loca.lt',
    'http://35.190.198.200:8000/',

]

CSRF_USE_SESSIONS = True
