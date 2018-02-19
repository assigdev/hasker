from django.http import JsonResponse


def vote_like(request, pk, model_class, qa_model_class):
    vote = model_class.voting(request.user, qa_model_class, pk, like=True)
    vote_count = vote.model.vote_count
    return JsonResponse({'vote_count': vote_count})


def vote_dislike(request, pk, model_class, qa_model_class):
    vote = model_class.voting(request.user, qa_model_class, pk, like=False)
    vote_count = vote.model.vote_count
    return JsonResponse({'vote_count': vote_count})
