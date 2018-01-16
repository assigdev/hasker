from django.db import models
from django.contrib.auth.models import AbstractUser


def get_avatar_path(instance, filename):
    return 'avatars/{0}/{1}/{2}/{3}'.format(
        instance.username[:1],
        instance.username[:2],
        instance.username,
        filename
    )


class User(AbstractUser):
    nickname = models.CharField(max_length=40, blank=True)
    avatar = models.ImageField(upload_to=get_avatar_path, blank=True, null=True)
