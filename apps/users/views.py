from django.views.generic import CreateView
from .forms import HaskerUserCreationForm


class CreateUserView(CreateView):
    template_name = 'users/sign_up.html'
    form_class = HaskerUserCreationForm
    success_url = '/'
