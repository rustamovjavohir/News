from pathlib import Path
from os.path import join as join_path
from os.path import exists as path_exists
from os.path import basename
from os import getenv
import os
import django_heroku

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-wag9eq044!&xh!c5teli7!v9f5uf%6=o2qyj0fp43(=2_74m1r'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'news',
    'accout',
    'ckeditor',
    'ckeditor_uploader'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'qalampir.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            join_path(BASE_DIR, 'templates'),
            join_path(BASE_DIR, 'news', 'templates'),
            join_path(BASE_DIR, 'accout', 'templates'),
        ]
        ,
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

WSGI_APPLICATION = 'qalampir.wsgi.application'
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'qalampir',
#         'USER': 'postgres',
#         'PASSWORD': '200527',
#         'HOST': 'localhost',
#         'POST': '5432',
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ddk2jio8uafoms',
        'USER': 'hvfhctvsrgxsyr',
        'PASSWORD': 'f17879b834ec0c9445aaaf9c4ca91908ab9f13058019a00d14a5ce557efc8272',
        'HOST': 'ec2-52-73-149-159.compute-1.amazonaws.com',
        'POST': '5432',
    }
}
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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
# STATICFILES_DIRS = [
#     join_path(BASE_DIR, 'static'),
# ]
STATIC_ROOT = join_path(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = join_path(BASE_DIR, 'media')
UPLOADS_ROOT = join_path(MEDIA_ROOT, 'uploads')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CKEDITOR_JQUERY_URL = 'http://libs.baidu.com/jquery/2.0.3/jquery.min.js'
CKEDITOR_UPLOAD_SLUGIFY_FILENAME = True
CKEDITOR_UPLOAD_PATH = "ck_uploads/"

# CKEDITOR CONFIGS
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': (
            ['div', 'Source', '-', 'Save', 'NewPage', 'Preview', '-', 'Templates'],
            ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Print', 'SpellChecker', 'Scayt'],
            ['Undo', 'Redo', '-', 'Find', 'Replace', '-', 'SelectAll', 'RemoveFormat'],
            ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton', 'HiddenField'],
            ['Bold', 'Italic', 'Underline', 'Strike', '-', 'Subscript', 'Superscript'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', 'Blockquote'],
            ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink', 'Anchor'],
            ['Image', 'Update', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak'],
            ['Styles', 'Format', 'Font', 'FontSize'],
            ['TextColor', 'BGColor'],
            ['Maximize', 'ShowBlocks', '-', 'About', 'pbckcode'],
        ),
    },
    'awesome_ckeditor': {
        'toolbar': (
            ['div', 'Source', '-', 'Save', 'NewPage', 'Preview', '-', 'Templates'],
            ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Print', 'SpellChecker', 'Scayt'],
            ['Styles', 'Format', 'Font', 'FontSize'],
        ),
    },

}

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = getenv('GMAIL_USER')
EMAIL_HOST_PASSWORD = getenv('GMAIL_PASSWORD')
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True

# Activate Django-Heroku.
django_heroku.settings(locals())
