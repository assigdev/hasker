from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, CreateView
from django.views.generic.edit import FormMixin
from django.http import Http404
from django.db.models import Q

from utils import get_unique_slug, send_email_from_template
from .forms import QuestionForm, AnswerForm
from .models import Question, Answer, Tag
from settings import FOR_AUTHOR_SUBJECT, SITE_URL


class QuestionListView(ListView):
    model = Question
    paginate_by = 20
    template_name = 'qa/list.html'
    context_object_name = 'questions'

    def get_queryset(self):
        queryset = super(QuestionListView, self).get_queryset()
        order_by = self.request.GET.get('order_by', None)
        if order_by == 'hot':
            queryset = queryset.order_by('-vote_count')
        return queryset

    def get_context_data(self, **kwargs):
        context = super(QuestionListView, self).get_context_data(**kwargs)
        order_by = self.request.GET.get('order_by', None)
        if order_by == 'hot':
            context['hot'] = True
        return context


class QuestionSearchListView(QuestionListView):
    template_name = 'qa/search.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        search_string = self.request.GET.get('q', None)
        if search_string is not None:
            queryset = queryset.filter(Q(title__icontains=search_string) | Q(content__icontains=search_string))
            queryset = queryset.order_by('-vote_count')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_q'] = self.request.GET.get('q')
        return context


class QuestionTagListView(QuestionListView):
    template_name = 'qa/tag.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        tag = self.kwargs.get('tag')
        queryset = queryset.filter(tags__title=tag)
        queryset = queryset.order_by('-vote_count')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_tag'] = 'tag:' + self.kwargs.get('tag')
        return context


class QuestionUserListView(QuestionListView):
    template_name = 'qa/user.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        username = self.kwargs.get('username', None)
        if username is None:
            raise Http404
        queryset = queryset.filter(create_by__username=username)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        username = self.kwargs.get('username', None)
        if username is not None:
            context['username'] = username
        return context


class QuestionCreateView(CreateView):
    template_name = 'qa/create.html'
    form_class = QuestionForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()  # for autocomplate
        return context

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.slug = get_unique_slug(obj.title, Question, 30)
        obj.create_by = self.request.user
        obj.save()
        obj.save_tags(self.request.POST.get('tags', False))
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
        context = super(QuestionDetailWithAnswerListView, self).get_context_data(**kwargs)
        context['question'] = self._get_question()
        return context

    def get_queryset(self):
        return self.model.objects.filter(question=self._get_question())

    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.create_by = self.request.user
        obj.save()
        send_email_from_template(
            obj.question.create_by.email,
            FOR_AUTHOR_SUBJECT,
            'mail/for_author.txt',
            {'question': obj.question, 'site_url': SITE_URL}
        )
        return HttpResponseRedirect(reverse('qa:detail',  kwargs={'slug': self._get_question().slug}))
