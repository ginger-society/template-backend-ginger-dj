"""Settings module"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
GDAL_LIBRARY_PATH = "/opt/homebrew/opt/gdal/lib/libgdal.dylib"
GEOS_LIBRARY_PATH = "/opt/homebrew/opt/geos/lib/libgeos_c.dylib"

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "ginger-insecure-u0j2maaxfoo8t1_l(l*asol9gw@(we8j=_lkn9m$dla55^(74@"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    "ginger.contrib.admin",
    "ginger.contrib.messages",
    "ginger.contrib.staticfiles",
    "ginger.rest_framework",
    "ginger.drf_yasg",
    "ginger.prometheus",
    "src",
]

MIDDLEWARE = [
    "ginger.middleware.security.SecurityMiddleware",
    "ginger.contrib.sessions.middleware.SessionMiddleware",
    "ginger.middleware.common.CommonMiddleware",
    "ginger.middleware.csrf.CsrfViewMiddleware",
    "ginger.contrib.messages.middleware.MessageMiddleware",
    "ginger.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "server.urls"

TEMPLATES = [
    {
        "BACKEND": "ginger.template.backends.ginger.GingerTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "ginger.template.context_processors.debug",
                "ginger.template.context_processors.request",
                "ginger.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "server.wsgi.application"


DATABASES = {  # pragma: no cover
    "default": {
        "ENGINE": "ginger.db.backends.postgresql_psycopg2",
        "NAME": 'Test-db',
        "USER": 'postgres',
        "PASSWORD": 'postgres',
        "HOST": 'localhost',
        "PORT": "5432",
    }
}

CACHES = {
    "default": {
        "BACKEND": "ginger.core.cache.backends.redis.RedisCache",
        "LOCATION": "redis://localhost:6379",
    }
}

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "ginger.db.models.BigAutoField"
