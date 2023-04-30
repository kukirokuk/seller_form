from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from .models import Question, Answer

def survey(request):
    first_question = Question.objects.first()
    context = {'question': first_question}
    return render(request, 'survey.html', context)

@require_POST
def submit_answer(request):
    question_id = request.POST['question_id']
    question = Question.objects.filter(id=question_id).first()
    if question:
        if question.qtype == 'text':
            answer_text = request.POST['answer_text']
            Answer.objects.create(question=question, text=answer_text)
        elif question.qtype == 'select':
            choice_id = request.POST['choice_id']
            choice = question.choices.filter(id=choice_id).first()
            Answer.objects.create(question=question, choice=choice)
        elif question.qtype == 'money':
            answer_money = request.POST['answer_money']
            Answer.objects.create(question=question, text=answer_money)
        next_question = Question.objects.filter(id__gt=question_id).first()
    else:
        next_question = Question.objects.first()
    context = {'question': next_question}
    return render(request, 'question.html', context)
