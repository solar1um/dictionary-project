from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from dictionary.models import Word, Meaning


@csrf_exempt
@api_view(['POST'])
def dictionary(request):
    if request.method == 'POST':
        query = request.POST.get('word')
        word = Word.objects.get(word=query).pk
        meanings = Meaning.objects.filter(current_word__pk=word)
    return HttpResponse({meanings}, status=status.HTTP_200_OK)
