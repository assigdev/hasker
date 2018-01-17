from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, CreateView

from utils import get_unique_slug
from .forms import QuestionForm
from .models import Question


class QuestionListView(ListView):
    model = Question
    paginate_by = 20
    template_name = 'qa/list.html'


class QuestionCreateView(CreateView):
    template_name = 'qa/create.html'
    form_class = QuestionForm

    def form_valid(self, form):
        form.send_email()
        obj = form.save(commit=False)
        obj.slug = get_unique_slug(obj.title, Question, 30)
        obj.create_by = self.request.user
        obj.save()
        return HttpResponseRedirect(self.get_success_url())
