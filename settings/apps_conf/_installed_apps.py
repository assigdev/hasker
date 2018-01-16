# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'django.contrib.sites',
    # 'django.contrib.sitemaps',
]

MY_APPS = [
    'apps.qa',
    # 'apps.users',
]


INSTALLED_APPS = [


]

INSTALLED_APPS = DJANGO_APPS + INSTALLED_APPS + MY_APPS
