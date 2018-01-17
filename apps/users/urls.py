from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import CreateUserView


urlpatterns = [
    url(r'^sign_in/$', auth_views.login, {'template_name': 'users/sign_in.html'}, name='sign_in'),
    url(r'^sign_up/$', CreateUserView.as_view(), name='sign_up'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
]
