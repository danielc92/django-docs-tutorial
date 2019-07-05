from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .forms import PollForm
from django.core.paginator import Paginator
from .models import Poll, Tag, Option
from django.urls import reverse
import json

def polls_index(request):

    context = {'title': 'Polls Home Page'}
    return render(request, 'index.html', context)

# View for voting
def polls_vote(request, question_id):
    return HttpResponse('polls vote')
    # question = get_object_or_404(Question, pk=question_id)

    # try:
    #     selected_choice = question.choice_set.get(pk=request.POST['choice'])

    # except (KeyError, Choice.DoesNotExist):
    #     return render(request, 'vote.html', {
    #         'title':'Polls Vote Page',
    #         'question': question,
    #         'error_message': "You didn't select a choice.",
    #     })
    # else:
    #     selected_choice.votes += 1
    #     selected_choice.save()

    #     return HttpResponseRedirect(reverse('polls-results', args=(poll.id,)))


def polls_result(request, question_id):

    poll = get_object_or_404(Poll, pk=poll_id)

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
def polls_list(request):

    polls = Poll.objects.all()

    paginator = Paginator(polls, 8)

    page = request.GET.get('page')

    data = paginator.get_page(page) 

    context = {'title': 'Polls List Page',
               'data':data}

    return render(request, 'poll-list.html', context)


# View which handles creating new questions through a form
# Everything will be automatically validated in this form
def polls_create(request):
    print('woo')
    if request.method == 'POST':
        form = PollForm(request.POST)
        if form.is_valid():
            new = form.save()

            for c in ['c1','c2','c3','c4']:
                text = form.data[c]
                if len(text) > 0:
                    Option.objects.create(text=text,poll=new)

    else:
        print('wood')
        form = PollForm()
        form_string = form.as_p()

    context = {'title':'Polls Create Question', 
                'form': form_string}

    return render(request, 'create-poll.html', context)