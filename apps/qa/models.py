from django.db import models
from django.utils.text import slugify

from apps.users.models import User


class Question(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=40)
    content = models.TextField()
    create_by = models.ForeignKey(User, related_name='questions')
    create_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tag')
    vote_count = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.title

    def get_answers_number(self):
        return self.answers.count()

    def get_votes_number(self):
        if hasattr(self, 'question_votes'):
            votes = self.question_votes
            return votes.get_like_users_number() + votes.get_dislike_users_number()
        return 0

    def save_tags(self, tag_names):
        if tag_names:
            tag_names_list = tag_names.split(',')
            for tag_name in tag_names_list:
                tag, created = Tag.objects.get_or_create(title=tag_name, slug=slugify(tag_name))
                tag.save()
                self.tags.add(tag)


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers')
    content = models.TextField()
    create_by = models.ForeignKey(User, related_name='answers')
    create_at = models.DateTimeField(auto_now_add=True)
    is_true = models.BooleanField(default=False)
    vote_count = models.SmallIntegerField(default=0)

    def __str__(self):
        return "answer {0} for question: {1}".format(self.id, self.question.title)


class Tag(models.Model):
    title = models.CharField(max_length=24)
    slug = models.SlugField(max_length=24)

    def __str__(self):
        return self.title
    
    def get_tag_for_search(self):
        return 'tag:{0}'.format(self.slug)
