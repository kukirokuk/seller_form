from django.db import models

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
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text