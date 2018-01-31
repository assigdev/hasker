# SECURITY WARNING: don't run with debug turned on in production!
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = True
SITE_URL = "http://localhost:8000"
ALLOWED_HOSTS = ['*']
