from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .forms import RawQuestionForm, RawChoiceForm
from django.core.paginator import Paginator
from .models import Question, Choice
from django.urls import reverse


def polls_index(request):

    context = {'title': 'Polls Home Page'}
    return render(request, 'index.html', context)

# View for voting
def polls_vote(request, question_id):

    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])

    except (KeyError, Choice.DoesNotExist):
        return render(request, 'vote.html', {
            'title':'Polls Vote Page',
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls-results', args=(question.id,)))

import json

def polls_result(request, question_id):

    question = get_object_or_404(Question, pk=question_id)

    choice_data = question.choice_set.all()

    choice_texts = []
    choice_votes = []

    for choice in choice_data:
        choice_texts.append(choice.choice_text)
        choice_votes.append(choice.votes)

    context = {'title':'Polls Results Page', 
    'question':question, 
    'choice_texts':choice_texts,
    'choice_votes':choice_votes,
    'choice_colours':['rgba(0, 209, 178, 0.55)'] * len(choice_data),
    'choice_border_colours': ['rgba(0, 209, 178, 0.9)'] * len(choice_data)}

    print(context)

    return render(request, 'results.html', context)


# View for questions list
def polls_questions_list(request):

    questions_list = Question.objects.all()
    paginator = Paginator(questions_list, 8)

    page = request.GET.get('page')

    data = paginator.get_page(page) 

    context = {'title': 'Polls List Page',
               'data':data}

    return render(request, 'questions-list.html', context)


# View which handles creating new questions through a form
# Everything will be automatically validated in this form
def polls_create_question(request):

    form = RawQuestionForm(request.GET)

    form_string = form.as_p()
    print(form_string)
    form_string = form_string.replace('<input', '<input class="input"')
    form_string = form_string.replace('<label', '<label class="label"')

    errors = None

    if request.method == "POST":
        form = RawQuestionForm(request.POST)

        if form.is_valid():

            Question.objects.create(**form.cleaned_data)
            return HttpResponse('<code>You have successfully added a new question.</code>')
        else:
            errors = form.errors

    context = {'title':'Polls Create Question', 'form': form_string, 'errors':errors}

    return render(request, 'create-question.html', context)


def polls_create_choice(request, question_id):

    form = RawChoiceForm(request.GET)
    errors = None

    if request.method == "POST":
        form = RawChoiceForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Choice.objects.create(question_id=question_id, **form.cleaned_data)
            return HttpResponse('<code>You have successfully added a new choice.</code>')
        else:
            errors = form.errors

    question = Question.objects.get(id=question_id)

    context = {'title':'Polls Create Choices','form': form, 'errors':errors, 'question':question}

    return render(request, 'create-choice.html', context)
