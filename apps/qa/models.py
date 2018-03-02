from django.db import models
from django.conf import settings
from django.db.models import Q
from django.http import Http404
from django.db import transaction
from hasker.settings import FOR_AUTHOR_SUBJECT, SITE_URL
from utils import get_unique_slug, send_email_from_template


class QuestionQuerySet(models.QuerySet):
    def search(self, search_string):
        queryset = self
        if search_string is not None and len(search_string) <= 200:
            queryset = queryset.filter(Q(title__icontains=search_string) | Q(content__icontains=search_string))
        return queryset.ordering()

    def get_user_questions(self, username):
        if username is None:
            raise Http404
        return self.filter(create_by__username=username)

    def ordering(self):
        return self.order_by('-vote_count', '-create_at')

    def ordering_if_hot(self, order_by):
        if order_by == 'hot':
            return self.ordering()
        return self


class Question(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=40)
    content = models.TextField()
    create_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='questions')
    create_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tag')
    vote_count = models.SmallIntegerField(default=0)
    objects = QuestionQuerySet.as_manager()

    def __str__(self):
        return self.title

    @transaction.atomic
    def save_with_arguments(self, user, tags):
        self.slug = get_unique_slug(self.title, Question, 30)
        self.create_by = user
        self.save()
        self.save_tags(tags)

    def get_answers_number(self):
        return self.answers.count()

    def get_votes_number(self):
        if hasattr(self, 'question_votes'):
            votes = self.question_votes
            return votes.get_like_users_number() + votes.get_dislike_users_number()
        return 0

    def save_tags(self, tag_names):
        tag_names = tag_names.replace(' ', '')
        if tag_names:
            tag_names_list = tag_names.split(',')
            for tag_name in tag_names_list:
                tag, created = Tag.objects.get_or_create(title=tag_name)
                tag.save()
                self.tags.add(tag)

    class Meta:
        ordering = ['-create_at']


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers')
    content = models.TextField()
    create_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='answers')
    create_at = models.DateTimeField(auto_now_add=True)
    is_true = models.BooleanField(default=False)
    vote_count = models.SmallIntegerField(default=0)

    def __str__(self):
        return "answer {0} for question: {1}".format(self.id, self.question.title)

    class Meta:
        ordering = ['-create_at']

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None, send_email=False):
        super().save()
        if send_email:
            question = self.question
            send_email_from_template(
                question.create_by.email,
                FOR_AUTHOR_SUBJECT,
                'mail/for_author.txt',
                {'question': question, 'site_url': SITE_URL}
            )


class Tag(models.Model):
    title = models.CharField(max_length=24)

    def __str__(self):
        return self.title
    
    def get_tag_for_search(self):
        return 'tag:{0}'.format(self.title)
