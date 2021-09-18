from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from dictionary.models import Word, Meaning


@csrf_exempt
@api_view(['POST'])
def dict(request):
    if request.method == 'POST':
        word = request.POST.get('word')
        word_pk = Word.objects.get(word=word).pk
        meanings = Meaning.objects.filter(word_fk__pk=word_pk)
    return HttpResponse({meanings}, status=status.HTTP_200_OK)
