import os
import raven


AUTH_USER_MODEL = 'users.User'
LOGIN_URL = '/user/login'
LOGIN_REDIRECT_URL = '/'

EMAIL_USE_SSL = True
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'noreply@bytehouse.ru'
EMAIL_HOST_PASSWORD = 'eilgyvt4815162342'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


DEFAULT_TO_EMAIL = 'asipipi@gmail.com'
FOR_AUTHOR_SUBJECT = 'Answer for your question'
DEFAULT_AVATAR_URL = '/static/img/default/default-avatar-male.png'
