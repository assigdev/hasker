
def get_unique_slug(for_slug, model, size=None):
    from django.utils.text import slugify
    import string
    import random

    slug = slugify(for_slug)
    if size:
        slug = slug[:size]
    while model.objects.filter(slug=slug).count() > 0 or len(slug) > 3:
        slug = slug[:-1] + random.choice(string.ascii_letters)
    return slug
