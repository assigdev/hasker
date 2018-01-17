from django.conf.urls import url
from .views import QuestionListView, QuestionCreateView


urlpatterns = [
    url(r'^$', QuestionListView.as_view(), name='list'),
    url(r'^question/create/$', QuestionCreateView.as_view(), name='create'),
    url(r'^question/(?P<slug>[\w-]+)$', QuestionListView.as_view(), name='detail'),
]
