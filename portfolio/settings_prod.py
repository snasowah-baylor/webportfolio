import os

import environ

from .settings import *  # noqa: F401,F403
from .settings import BASE_DIR

env = environ.Env()

DEBUG = False

SECRET_KEY = env("SECRET_KEY")

ALLOWED_HOSTS = env("ALLOWED_HOSTS", default="").split(",")

DATABASES = {
    "default": env.db("DATABASE_URL", default=f"sqlite:///{os.path.join(BASE_DIR, 'db.sqlite3')}"),
}

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = "DENY"
