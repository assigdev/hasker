from django.db import models
from apps.qa.models import Question, Answer
from apps.users.models import User
from django.db import transaction


class VoteModelExample(models.Model):
    vote_count = models.SmallIntegerField(default=0)


class AbstractVote(models.Model):
    model = models.OneToOneField(VoteModelExample)
    like_users = models.ManyToManyField(User, related_name='like_answers')
    dislike_users = models.ManyToManyField(User, related_name='dislike_answers')

    class Meta:
        abstract = True

    def vote_count_up(self):
        self.model.vote_count += 1

    def vote_count_down(self):
        self.model.vote_count -= 1

    @transaction.atomic
    def like(self, user):
        if self.like_users.filter(pk=user.pk).exists():
            self.like_users.remove(user)
            self.vote_count_down()
        else:
            if self.dislike_users.filter(pk=user.pk).exists():
                self.dislike_users.remove(user)
                self.vote_count_up()
            self.like_users.add(user)
            self.vote_count_up()

    @transaction.atomic
    def dislike(self, user):
        if self.dislike_users.filter(pk=user.pk).exists():
            self.dislike_users.remove(user)
            self.vote_count_up()
        else:
            if self.like_users.filter(pk=user.pk).exists():
                self.like_users.remove(user)
                self.vote_count_down()
            self.dislike_users.add(user)
            self.vote_count_down()

    def get_like_users_number(self):
        return self.like_users.count()

    def get_dislike_users_number(self):
        return self.dislike_users.count()


class QuestionVote(AbstractVote):
    model = models.OneToOneField(Question, related_name='question_votes')
    like_users = models.ManyToManyField(User, related_name='like_questions')
    dislike_users = models.ManyToManyField(User, related_name='dislike_questions')


class AnswerVote(AbstractVote):
    model = models.OneToOneField(Answer, related_name='answer_votes')
    like_users = models.ManyToManyField(User, related_name='like_answers')
    dislike_users = models.ManyToManyField(User, related_name='dislike_answers')
