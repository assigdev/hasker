from django.test import TestCase
from ..models import Question, Answer, Tag
from apps.users.models import User


class QuestionTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User(username='user1', password='user_pass')
        user.save()

    def test_create(self):
        user = User.objects.first()
        q = Question.objects.create(title='title', content='content', slug='title', create_by=user)
        self.assertEquals(q.title, 'title')
        self.assertEquals(q.content, 'content')
        self.assertEquals(q.slug, 'title')
        self.assertEquals(q.create_by.username, user.username)

    def test_save_tags(self):
        user = User.objects.first()
        q = Question.objects.create(title='title', content='content', slug='title', create_by=user)
        q.save_tags('python,django,mango')
        self.assertEquals(q.tags.count(), 3)
        self.assertEquals(q.tags.get(title='python').title, 'python')
        self.assertEquals(q.tags.get(title='django').title, 'django')
        self.assertEquals(q.tags.get(title='mango').title, 'mango')

        q = Question.objects.create(title='title2', content='content2', slug='title2', create_by=user)

        q.save_tags('cython, django, mango, gango')
        self.assertEquals(q.tags.count(), 4)
        self.assertEquals(q.tags.get(title='cython').title, 'cython')
        self.assertEquals(q.tags.get(title='django').title, 'django')
        self.assertEquals(q.tags.get(title='mango').title, 'mango')
        self.assertEquals(q.tags.get(title='gango').title, 'gango')
