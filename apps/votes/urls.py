from django.conf.urls import url
from .views import vote_like, vote_dislike
from .models import QuestionVote, AnswerVote
from apps.qa.models import Question, Answer


urlpatterns = [
    url(
        r'^question/(?P<pk>\d+)/like/$',
        vote_like,
        {'model_class': QuestionVote, 'qa_model_class': Question},
        name='question_like',
        ),
    url(
        r'^question/(?P<pk>\d+)/dislike/$',
        vote_dislike,
        {'model_class': QuestionVote, 'qa_model_class': Question},
        name='question_dislike'
    ),
    url(r'^answer/(?P<pk>\d+)/like/$',
        vote_like,
        {'model_class': AnswerVote, 'qa_model_class': Answer},
        name='answer_like'
        ),
    url(r'^answer/(?P<pk>\d+)/dislike/$',
        vote_dislike,
        {'model_class': AnswerVote, 'qa_model_class': Answer},
        name='answer_dislike'
        ),
]
