from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, CreateView
from django.views.generic.edit import FormMixin

from utils import get_unique_slug
from .forms import QuestionForm, AnswerForm
from .models import Question, Answer, Tag


class QuestionListView(ListView):
    model = Question
    paginate_by = 20
    template_name = 'qa/list.html'
    context_object_name = 'questions'


class QuestionSearchListView(QuestionListView):
    template_name = 'qa/search.html'

    def get_queryset(self):
        queryset = []
        search_string = self.request.GET.get('q', None)
        print(search_string)
        print('*******************************')
        if search_string is not None:
            queryset = self.model.objects.filter(title__icontains=search_string)
            queryset = queryset.order_by('title')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_q'] = self.request.GET.get('q', None)
        return context


class QuestionTagListView(QuestionListView):
    template_name = 'qa/tag.html'

    def get_queryset(self):
        queryset = []
        tag = self.kwargs.get('tag', None)
        if tag is not None:
            queryset = self.model.objects.filter(tags__title=tag)
            queryset = queryset.order_by('title')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_tag'] = 'tag:' + self.kwargs.get('tag', '')
        return context


class QuestionCreateView(CreateView):
    template_name = 'qa/create.html'
    form_class = QuestionForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()  # for autocomplate
        return context

    def get_success_url(self):
        return reverse('qa:detail')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.slug = get_unique_slug(obj.title, Question, 30)
        obj.create_by = self.request.user
        obj.save()
        obj.save_tags(self.request.POST.get('tags', False))
        print(obj.slug)
        return HttpResponseRedirect(reverse('qa:detail', kwargs={'slug': obj.slug}))


class QuestionDetailWithAnswerListView(FormMixin, ListView):
    template_name = 'qa/detail.html'
    context_object_name = 'answers'
    model = Answer
    paginate_by = 30
    question = None
    form_class = AnswerForm

    def get_initial(self):
        return {'question': self._get_question().id}

    def _get_question(self):
        if self.question is None:
            slug = self.kwargs.get('slug', None)
            if slug:
                obj = get_object_or_404(Question, slug=slug)
                self.question = obj
            else:
                raise Http404
        return self.question

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['question'] = self._get_question()
        return context

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['current_q'] = self.request.GET.get('q', None)
    #     return context

    def get_queryset(self):
        return self.model.objects.filter(question=self._get_question())

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.create_by = self.request.user
        obj.save()
        return HttpResponseRedirect(reverse('qa:detail',  kwargs={'slug': self._get_question().slug}))
