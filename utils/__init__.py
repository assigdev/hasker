from django.core.mail import send_mail
from django.template import Context
from django.template.loader import get_template
from settings import DEFAULT_FROM_EMAIL


def get_unique_slug(for_slug, model, size=None):
    from django.utils.text import slugify
    import string
    import random

    slug = slugify(for_slug)
    if size:
        slug = slug[:size]
    while model.objects.filter(slug=slug).count() > 0 or len(slug) < 3:
        slug = slug[:-1] + random.choice(string.ascii_letters)
    return slug


def send_email_from_template(recipient, subject, message_template_name, context, ):
    template = get_template(message_template_name)
    message = template.render(context)
    send_mail(
        subject,
        message,
        DEFAULT_FROM_EMAIL,
        [recipient],
        fail_silently=False,
    )
