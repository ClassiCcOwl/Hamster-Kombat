from .base import *  # noqa
from .base import env

SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="8j48laPaYNICwHG1UqbPNosk3ZJYgGuJMV5BVUfJANA11YQRGC4",
)


ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["*"])
