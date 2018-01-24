from .models import Question, Answer
from django import forms


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = (
            "title",
            "content",
        )


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = (
            "question",
            "content",
        )
        widgets = {'question': forms.HiddenInput()}

