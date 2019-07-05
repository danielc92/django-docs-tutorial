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


def polls_view(request, poll_id):

    poll = get_object_or_404(Poll, pk=poll_id)
    
    options = poll.options.all()
    option_votes = [o.votes for o in options]
    option_names = [o.text for o in options]   

    context = { 'poll': poll, 'votes': option_votes, 'names': option_names}

    return render(request, 'poll-detail.html', context)


def option_vote(request, option_id):

    option = get_object_or_404(Option, pk=option_id)
    poll_id = option.poll.id
    option.votes = option.votes + 1
    option.save()

    return HttpResponseRedirect(reverse('polls-view', args=(poll_id,)))


def polls_list(request):

    polls = Poll.objects.all()

    paginator = Paginator(polls, 8)

    page = request.GET.get('page')

    data = paginator.get_page(page) 

    context = {'title': 'Polls List Page',
               'data':data}

    return render(request, 'poll-list.html', context)



def polls_create(request):

    if request.method == 'POST':
        form = PollForm(request.POST)
        if form.is_valid():
            new = form.save()

            for c in ['c1','c2','c3','c4']:
                text = form.data[c]
                if len(text) > 0:
                    Option.objects.create(text=text,poll=new)
            
            return HttpResponseRedirect(reverse('polls-list'))
    else:
        form = PollForm()
    
    form = form.as_p()
    form = form\
                .replace('<input', '<input class="input"')\
                .replace('<label', '<label class="label"')\
                .replace('<select', '<div class="select is-multiple"><select')\
                .replace('</select>', '</select></div>')

    context = {'title':'Polls Create Question', 
                'form': form}

    return render(request, 'create-poll.html', context)