from django.db import models
from apps.users.models import User


class Question(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=40)
    content = models.TextField()
    create_by = models.ForeignKey(User, related_name='questions')
    create_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.title


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers')
    content = models.TextField()
    create_by = models.ForeignKey(User, related_name='answers')
    create_at = models.DateTimeField(auto_now_add=True)
    is_true = models.BooleanField(default=False)

    def __str__(self):
        return "answer {0} for question: {1}".format(self.id, self.question.title)


class Tag(models.Model):
    title = models.CharField(max_length=24)
    slug = models.SlugField(max_length=24)

    def __str__(self):
        return self.title
