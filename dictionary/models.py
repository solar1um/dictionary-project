from django.db import models


class Word(models.Model):
    word = models.CharField(max_length=50)

    def __str__(self):
        return self.word


class Meaning(models.Model):
    current_word = models.ForeignKey(Word, on_delete=models.CASCADE, related_name='current_wrd')
    word_meaning = models.TextField(max_length=500)

    def __str__(self):
        return self.word_meaning
