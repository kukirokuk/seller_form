from django.db import models
from django.utils import timezone


class Question(models.Model):
    TEXT = 'text'
    SELECT = 'select'
    MONEY = 'money'
    HIDDEN = 'hidden'
    TYPE_CHOICES = [
        (TEXT, 'Text'),
        (SELECT, 'Select'),
        (MONEY, 'Money'),
        (HIDDEN, 'Hidden'),
    ]

    text = models.CharField(max_length=200)
    qtype = models.CharField(choices=TYPE_CHOICES, default=TEXT, max_length=10)
    is_required = models.BooleanField(default=True)

    def __str__(self):
        return self.text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text


class Survey(models.Model):
    survey_id = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.survey_id

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name='answers')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text