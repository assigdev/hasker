from django.http import JsonResponse
from .models import Answer


def set_answer_true_view(request, pk):
    error = None
    reset = False  # if click twice reset is_true
    try:
        answer = Answer.objects.get(pk=pk)
        if request.user == answer.question.create_by:
            if answer.is_true is True:
                answer.is_true = False
                reset = True
            else:
                answer.is_true = True
                answer.question.answers.update(is_true=False)
            answer.save()
        else:
            error = 'You are not the creator of the question'
    except Answer.DoesNotExist:
        error = 'Answer does not exist'
    return JsonResponse({'error': error, 'reset': reset})
