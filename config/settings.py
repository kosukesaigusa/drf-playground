"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.2.15.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os.path
from datetime import timedelta
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # サードパーティのアプリケーション
    "rest_framework",
    "djoser",
    "corsheaders",
    # 自作アプリケーション
    "apiv1.apps.Apiv1Config",
    "shop.apps.ShopConfig",
]

MIDDLEWARE = [
    # フロントエンドの Web サーバのオリジンからの API アクセスを許可するために
    # django-cors-headers パッケージを使用して CORS のホワイトリストを設定する。
    #
    # - フロントエンドの配信用エンドポイント http://127.0.0.1:8000
    # - Django の REST API のエンドポイント https://127.0.0.1:8000/api/v1/...
    #
    # というようにポート番号が異なるため？
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            # テンプレートファイルの検索ディレクトリに BASE_DIR/templates を指定
            os.path.join(BASE_DIR, "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# ログイン・ログアウト成功時のリダイレクト先の設定
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "rest_framework:login"


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

# 言語コードを修正
LANGUAGE_CODE = "ja"

# タイムゾーンを修正
TIME_ZONE = "Asia/Tokyo"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"

# 静的ファイルの検索ディレクトリに BASE_DIR/static を指定
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# REST Framework
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": {
        # DRF の Cookie 認証の設定
        # "rest_framework.authentication.SessionAuthentication",
        # DRF の JWT 認証の設定
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    },
    # rest_framework/settings.py におけるデフォルト設定。
    # ブラウザ上でリクエストおよびレスポンスのサマリを確認するなどの機能が利用できる。
    # 本番環境では無効化するべきである。
    # "DEFAULT_RENDERER_CLASSES": [
    #     "rest_framework.renderers.JSONRenderer",
    #     "rest_framework.renderers.BrowsableAPIRenderer",
    # ],
}

# simplejwt の設定
SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ("JWT",),
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
}

# CORS の設定
CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
    "https://127.0.0.1:8080",
]

try:
    from .local import *
except ImportError:
    pass
