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
    return HttpResponse({meanings: True}, status=status.HTTP_200_OK)







# def dictionary(request):
#     if request.method == 'POST':
#         word = request.POST.get('word')
#         all_words = Word.objects.all()
#         print(all_words.get(id=2))
#         meaning = Meaning.objects.get(id=2)
#         print(meaning)
#     return HttpResponse({word: True}, status=status.HTTP_200_OK)

# def dictionary(request):
#     if request.method == 'POST':
#         word = request.POST.get('word')
#         # all_words = Word.objects.get(word=word).pk
#         # all_meanings = Meaning.objects.filter(pk=all_words)
#         # print(all_words)
#         # print(all_meanings)
#         # all_words = Meaning.objects.filter(current_word__word=word)
#         all_words = Meaning.objects.values().filter(id=1).filter('word_meaning')
#         print(all_words)
#     return HttpResponse({'success': True}, status=status.HTTP_200_OK)