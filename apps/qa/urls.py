from django.conf.urls import url
from .views import (
    QuestionListView,
    QuestionCreateView,
    QuestionDetailWithAnswerListView,
    QuestionSearchListView,
    QuestionTagListView
)
from .views_ajax import set_answer_true_view

urlpatterns = [
    url(r'^$', QuestionListView.as_view(), name='list'),
    url(r'^ask/$', QuestionCreateView.as_view(), name='create'),
    url(r'^search$', QuestionSearchListView.as_view(), name='search'),
    url(r'^question/(?P<slug>[\w-]+)/$', QuestionDetailWithAnswerListView.as_view(), name='detail'),
    url(r'^tag/(?P<tag>[\w-]+)/$', QuestionTagListView.as_view(), name='tag'),
    url(r'^set_answer_true/(?P<pk>\d+)$', set_answer_true_view, name='set_answer_true'),
]
