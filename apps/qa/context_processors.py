from .models import Question


def ad(request):
    return {
        'trand_questions': Question.objects.order_by('-vote_count', 'title')[:20],
    }