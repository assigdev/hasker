from django.http import JsonResponse


def vote_like(request, pk, model_class, qa_model_class):
    qa_object = qa_model_class.objects.get(pk=pk)
    vote, created = model_class.objects.get_or_create(model=qa_object)
    vote.like(request.user)
    vote.model.save()
    vote_count = vote.model.vote_count
    return JsonResponse({'vote_count': vote_count})


def vote_dislike(request, pk, model_class, qa_model_class):
    qa_object = qa_model_class.objects.get(pk=pk)
    vote, created = model_class.objects.get_or_create(model=qa_object)
    vote.dislike(request.user)
    vote.model.save()
    vote_count = vote.model.vote_count
    return JsonResponse({'vote_count': vote_count})
