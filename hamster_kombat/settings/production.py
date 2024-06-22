from .base import *  # noqa
from .base import env

SECRET_KEY = env("DJANGO_SECRET_KEY")


ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["*"])
CSRF_TRUSTED_ORIGINS = ["https://hamster-kombat.chbk.run","https://api.boardingle.ir"]
