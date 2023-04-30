from django.contrib import admin
from .models import Question, Choice, Answer

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

admin.site.register(Answer)
admin.site.register(Question, QuestionAdmin)
