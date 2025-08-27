import os
from pathlib import Path

# -----------------------------
# Basic paths & secret key
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = '^rhmj$0u%!hsz)%thrwvfni#ied_8$#p+fg0weejwvj!f6o-ct'
DEBUG = True
ALLOWED_HOSTS = ['*']

# -----------------------------
# HTTPS / CSRF settings
# -----------------------------
USE_HTTPS = os.getenv('USE_HTTPS', 'False') == 'True'

CSRF_TRUSTED_ORIGINS = [
    "http://localhost",
    "http://127.0.0.1",
    "http://192.168.0.100",  # local IP
    "https://6eab714d5021.ngrok-free.app",  # ngrok URL
]

if USE_HTTPS:
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SAMESITE = "None"
    SESSION_COOKIE_SAMESITE = "None"
else:
    CSRF_COOKIE_SECURE = False
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SAMESITE = "Lax"
    SESSION_COOKIE_SAMESITE = "Lax"

# -----------------------------
# Installed apps
# -----------------------------
INSTALLED_APPS = [
    'dada.apps.DadaConfig',  # keep only this
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'widget_tweaks',

]


# -----------------------------
# Middleware
# -----------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# -----------------------------
# URLs & templates
# -----------------------------
ROOT_URLCONF = 'bohemia.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'template'],  # template folder
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'bohemia.wsgi.application'

# -----------------------------
# Database
# -----------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# -----------------------------
# Static files
# -----------------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']  # dev
STATIC_ROOT = BASE_DIR / 'staticfiles'  # production

# -----------------------------
# Authentication
# -----------------------------
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'login'
AUTH_USER_MODEL = 'dada.CustomUser'  # ✅ use your custom user model
