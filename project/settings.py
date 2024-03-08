"""
Settings
"""

from wav4django.settings import SettingsFromTOML
from pathlib import Path
import sys


# ----------------------------------------------------------------------
# Environment-Specific Settings
# ----------------------------------------------------------------------
if sys.version_info < (3, 11):
    raise EnvironmentError("Python version 3.11 or later is required")

BASE_DIR = Path(__file__).resolve().parents[1]
PROJECT_DIR = BASE_DIR / "project"

toml = SettingsFromTOML(env_var="CFC_SETTINGS", base_dir=BASE_DIR)

DEBUG = toml.get("DEBUG")
SECRET_KEY = toml.get("SECRET_KEY")
ALLOWED_HOSTS = toml.get("ALLOWED_HOSTS")
INTERNAL_IPS = toml.get("INTERNAL_IPS", [])

DATABASES = dict(default=toml.get("DATABASES.default"))
STORAGES = toml.get("STORAGES")
EMAIL_BACKEND = toml.get("EMAIL_BACKEND")
SOCIAL_ACCOUNTS = toml.get("SOCIALACCOUNT_PROVIDERS")

STATICFILES_FINDERS = toml.get(
    "STATICFILES_FINDERS",
    [
        "django.contrib.staticfiles.finders.FileSystemFinder",
        "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    ],
)
STATICFILES_DIRS = toml.get("STATICFILES_DIRS", [BASE_DIR / "project/static"])
STATIC_ROOT = toml.get("STATIC_ROOT", BASE_DIR / "static")
STATIC_URL = toml.get("STATIC_URL", "/static/")

MEDIA_ROOT = toml.get("MEDIA_ROOT", BASE_DIR / "media")
MEDIA_URL = toml.get("MEDIA_URL", "/media/")

# ----------------------------------------------------------------------
# All-Environments Settings
# ----------------------------------------------------------------------
# -------- Application Definition
INSTALLED_APPS = [
    "cfc",
    "search",
    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",
    "wagtail",
    "modelcluster",
    "taggit",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    DEBUG and "debug_toolbar",
]
INSTALLED_APPS = [x for x in INSTALLED_APPS if isinstance(x, str)]

MIDDLEWARE = [
    DEBUG and "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
]
MIDDLEWARE = [x for x in MIDDLEWARE if isinstance(x, str)]

ROOT_URLCONF = "project.urls"

WSGI_APPLICATION = "project.wsgi.application"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [PROJECT_DIR / "templates"],
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

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# -------- Internationalization / i18n
# https://docs.djangoproject.com/en/5.0/topics/i18n/
LANGUAGE_CODE = "en-ca"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True


# -------- User / Authentication
AUTH_USER_MODEL = "cfc.User"
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


# -------- Wagtail
WAGTAIL_SITE_NAME = "cfc"
# https://docs.wagtail.org/en/stable/topics/search/backends.html
WAGTAILSEARCH_BACKENDS = {
    "default": {
        "BACKEND": "wagtail.search.backends.database",
    }
}
# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
WAGTAILADMIN_BASE_URL = "http://example.com"


# -------- Other Settings
OBFUSCATE_CONFIG = {
    "min_length": 5,
    "alphabet": "VDE9N7YWTFJHAPM2RUGB8CZ53L4XS6QK",
}
