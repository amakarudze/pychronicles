from .base import * # noqa: F403


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY", "heythere!") # noqa: F405

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

MIDDLEWARE += [ # noqa: F405
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
] 

INSTALLED_APPS += ["django.contrib.staticfiles"] # noqa: F405

STATICFILES_DIRS = [BASE_DIR / "static"] # noqa: F405

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}

SILENCED_SYSTEM_CHECKS = ['django_recaptcha.recaptcha_test_key_error']
