from pathlib import Path
import environ
from datetime import timedelta

env = environ.Env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

APP_DIR = BASE_DIR / "core_apps"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DJANGO_DEBUG", False)


# Application definition

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "rest_framework",
    "django_filters",
    "drf_yasg",
    "corsheaders",
    "request",
    "rest_framework.authtoken",
    "rest_framework_simplejwt.token_blacklist",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "dj_rest_auth",
    "dj_rest_auth.registration",
]

LOCAL_APPS = [
    "core_apps.users",
    "core_apps.game",
    "core_apps.common",
    "core_apps.crawler",
    "core_apps.daily",
    "core_apps.profiles",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "request.middleware.RequestMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = "hamster_kombat.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "hamster_kombat.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("PGDATABASE"),
        "USER": env("PGUSER"),
        "PASSWORD": env("PGPASSWORD"),
        "HOST": env("PGHOST"),
        "PORT": env("PGPORT", default=5432),
        "OPTIONS": {
            "sslmode": "require",
            "options": env("PGENDPOINT"),
        },
    }
}

AUTH_USER_MODEL = "users.User"
# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    "django.contrib.auth.hashers.ScryptPasswordHasher",
]
# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

LOGIN_URL = "api/v1/auth/login/"
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

STATIC_URL = "static/"
STATIC_ROOT = str(BASE_DIR / "static")

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "dj_rest_auth.jwt_auth.JWTCookieAuthentication"
        # "rest_framework.authentication.TokenAuthentication",
        # "rest_framework.authentication.BasicAuthentication",
        # "rest_framework.authentication.SessionAuthentication",
    ],
    # "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.IsAuthenticated"],
    # "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
}

SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ("Bearer",),
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=15),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "SIGNING_KEY": env("SIGNING_KEY"),
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
}


REST_AUTH = {
    "USE_JWT": True,
    "JWT_AUTH_HTTPONLY": False,
    "JWT_AUTH_COOKIE": "boardingle-access-token",
    "JWT_AUTH_REFRESH_COOKIE": "boardingle-refresh-token",
    "REGISTER_SERIALIZER": "core_apps.users.serializers.CustomRegisterSerializer",
    "LOGIN_SERIALIZER": "core_apps.users.serializers.CustomLoginSerializer",
}

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]
ACCOUNT_EMAIL_VERIFICATION = "none"
ACCOUNT_EMAIL_REQUIRED = False
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_USER_MODEL_EMAIL_FIELD = None
ACCOUNT_AUTHENTICATION_METHOD = "username"
ACCOUNT_USER_MODEL_USERNAME_FIELD = "username"

MEDIA_URL = "/media/"
MEDIA_ROOT = str(BASE_DIR / "media/")

# CORS_URLS_REGEX = r"*"


REQUEST_IGNORE_USERNAME = env.list("REQUEST_IGNORE_USERNAME", default=[])
