from django.db import models
from django.contrib.auth.models import AbstractUser
from settings import DEFAULT_AVATAR_URL


def get_avatar_path(instance, filename):
    return 'avatars/{0}/{1}/{2}/{3}'.format(
        instance.username[:1],
        instance.username[:2],
        instance.username,
        filename
    )


class User(AbstractUser):
    avatar = models.ImageField(upload_to=get_avatar_path)

    def get_avatar_url(self):
        if self.avatar:
            return self.avatar.url
        else:
            return DEFAULT_AVATAR_URL
