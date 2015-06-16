# This file is part of Shoop Wintergear Demo.
#
# Copyright (c) 2012-2015, Shoop Ltd. All rights reserved.
#
# This source code is licensed under the AGPLv3 license found in the
# LICENSE file in the root directory of this source tree.
from shoop.addons import add_enabled_addons
import os

BASE_DIR = os.path.realpath(
    os.path.join(os.path.dirname(__file__), "..", ".."))
SECRET_KEY = "Shhhhh"
DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []

MEDIA_ROOT = os.path.join(BASE_DIR, "var", "media")
STATIC_ROOT = os.path.join(BASE_DIR, "var", "static")
MEDIA_URL = "/media/"

SHOOP_ENABLED_ADDONS_FILE = os.path.join(BASE_DIR, "var", "enabled_addons")
INSTALLED_APPS = add_enabled_addons(SHOOP_ENABLED_ADDONS_FILE, (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    ####
    'shoop_demo',
    'wintergear_theme',
    'wintergear_demo_content',
    ####
    'django_jinja',
    'filer',
    'easy_thumbnails',
    'shoop.core',
    'shoop.simple_pricing',
    'shoop.simple_supplier',
    'shoop.default_tax',
    'shoop.front',
    'shoop.front.apps.registration',
    'shoop.front.apps.auth',
    'shoop.front.apps.customer_information',
    'shoop.front.apps.personal_order_history',
    'shoop.front.apps.simple_order_notification',
    'shoop.front.apps.simple_search',
    'shoop.admin',
    'shoop.addons',
    'shoop.testing',
    'bootstrap3',
    'shoop.notify',
    'shoop.simple_cms',
    'shoop.stripe',

    'registration',
))

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'shoop.front.middleware.ProblemMiddleware',
    'shoop.front.middleware.ShoopFrontMiddleware',
)

ROOT_URLCONF = 'shoop_demo.urls'
WSGI_APPLICATION = 'shoop_demo.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'TEST': {
            'NAME': os.path.join(BASE_DIR, 'db_test.sqlite3'),
        }
    }
}

LANGUAGE_CODE = 'en'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = '/static/'
LOGIN_REDIRECT_URL = '/'
SOUTH_TESTS_MIGRATE = False  # Makes tests that much faster.

LANGUAGES = [
    ('en', 'English'),
    ('fi', 'Finnish'),
]

PARLER_DEFAULT_LANGUAGE_CODE = "en"

PARLER_LANGUAGES = {
    None: [{"code": c, "name": n} for (c, n) in LANGUAGES],
    'default': {
        'hide_untranslated': False,
    }
}


TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.request",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages"
)

TEMPLATES = [
    {
        "BACKEND": "django_jinja.backend.Jinja2",
        "APP_DIRS": True,
        "OPTIONS": {
            "match_extension": ".jinja",
            "context_processors": TEMPLATE_CONTEXT_PROCESSORS,
            "newstyle_gettext": True,
        },
        "NAME": "jinja2",
    },
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": TEMPLATE_CONTEXT_PROCESSORS,
        }
    },
]


SESSION_SERIALIZER = "django.contrib.sessions.serializers.PickleSerializer"

SHOOP_PAYMENT_MODULE_IMPLEMENTATIONS = {
    "pseudo": "shoop.testing.pseudo_payment.PseudoPaymentMethodModule",
}

SHOOP_BASKET_COMMAND_DISPATCHER_SPEC = (
    "shoop_demo.basket_command_dispatcher:WintergearBasketCommandDispatcher")
SHOOP_BASKET_VIEW_SPEC = "shoop_demo.views.basket:WintergearBasketView"


def configure(setup):
    setup.commit(globals())
