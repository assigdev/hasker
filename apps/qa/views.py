from django.views.generic import ListView
from .models import Question


class QuestionListView(ListView):
    model = Question
    paginate_by = 20
    template_name = 'qa/list.html'
