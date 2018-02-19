from django.db import models
from django.contrib.auth.models import AbstractUser
from hasker.settings import DEFAULT_AVATAR_URL


HASH_CHUNK_SIZE = 65536


def get_avatar_path(instance, filename):
    import os.path
    import hashlib
    parts = os.path.splitext(filename)
    ctx = hashlib.sha256()
    if instance.avatar.multiple_chunks():
        for data in instance.avatar.chunks(HASH_CHUNK_SIZE):
            ctx.update(data)
    else:
        ctx.update(instance.avatar.read())
    hex_path = ctx.hexdigest()
    return 'avatars/{0}/{1}/{2}{3}'.format(
        hex_path[0:2],
        hex_path[2:18],
        hex_path[18:34],
        parts[1]
    )


class User(AbstractUser):
    avatar = models.ImageField(upload_to=get_avatar_path)

    def get_avatar_url(self):
        if self.avatar:
            return self.avatar.url
        else:
            return DEFAULT_AVATAR_URL
