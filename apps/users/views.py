from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.views.generic import CreateView, UpdateView

from .forms import HaskerUserCreationForm, UserUpdateForm


class UserCreateView(CreateView):
    template_name = 'users/sign_up.html'
    form_class = HaskerUserCreationForm

    def get_success_url(self):
        return reverse('users:setting')

    def form_valid(self, form):
        messages.success(self.request, 'The account was successfully created. Now you can enter')
        return super(UserCreateView, self).form_valid(form)


class UserUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "users/update_user.html"
    form_class = UserUpdateForm

    def get_success_url(self):
        return reverse('users:setting')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, 'Settings successfully saved')
        return super(UserUpdateView, self).form_valid(form)
