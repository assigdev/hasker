from django.test import TestCase, Client
from ..views import QuestionListView
from ..models import Question
from django.core.urlresolvers import reverse


class QuestionListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Question.create()

    def setUp(self):
        self.client = Client()

    def test_list(self):
        response = self.client.get(reverse('qa:list'))

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

    def test_details2(self):
        response = self.client.get(reverse('qa:list'))

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the rendered context contains 5 customers.
        # self.assertEqual(len(response.context['customers']), 5)