import uuid

from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect  
from .models import Question, Answer, Survey


def survey(request):
    if 'survey_id' not in request.session:
        request.session['survey_id'] = str(uuid.uuid4())
        
    first_question = Question.objects.first()
    context = {'question': first_question}
    return render(request, 'survey.html', context)

@require_POST
@csrf_exempt
def submit_answer(request):
    question_id = request.POST['question_id']
    question = Question.objects.filter(id=question_id).first()
    survey_id = request.session['survey_id']
    if question:
        if question.qtype == 'text':
            answer_text = request.POST['answer_text']
        elif question.qtype == 'select':
            choice_id = request.POST['choice_id']
            answer_text = question.choices.filter(id=choice_id).first()

        survey, created = Survey.objects.get_or_create(survey_id=survey_id)
        Answer.objects.create(question=question, survey=survey, text=answer_text)
        next_question = Question.objects.filter(id__gt=question_id).first()
    else:
        next_question = Question.objects.first()
    
            # Clear session if there are no more questions in the survey
    if not next_question:
        request.session.flush()

        # Redirect to thank you page
        return redirect('thank_you')

    context = {'question': next_question}
    return render(request, 'question.html', context)

def results(request):
    # get all unique survey ids
    survey_ids = Answer.objects.values_list('survey_id', 'survey__survey_id').distinct()
    # for each survey id, get all answers and create a dictionary for the survey
    surveys = []
    for survey_id in survey_ids:
        survey_lst = []
        answers = Answer.objects.filter(survey_id=survey_id)
        survey_lst.extend(survey_id)
        for answer in answers:
            survey_lst.append(answer.text)
        surveys.append(survey_lst)
    # render the results template with the surveys
    return render(request, 'results.html', {'survey_results': surveys})

@csrf_exempt
def clear_session(request):
    request.session.flush()
    return redirect('/')

def thank_you(request):
    return render(request, 'thank_you.html')