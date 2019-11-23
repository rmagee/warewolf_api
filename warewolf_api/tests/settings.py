# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

import django

DEBUG = True
USE_TZ = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "jv5gy%g@jy6%8-ri744b3vx*8iwu*9#$f+bagneqq2%gb2p-j&"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

ROOT_URLCONF = "warewolf_api.urls"

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sites",
    "quartet_masterdata",
    "quartet_epcis",
    "warewolf_api.apps.WarewolfApiConfig",
    "quartet_output.apps.QuartetOutputConfig",
    "quartet_capture"
]

SITE_ID = 1

if django.VERSION >= (1, 10):
    MIDDLEWARE = ()
else:
    MIDDLEWARE_CLASSES = ()

