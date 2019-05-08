from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
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
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls-results', args=(question.id,)))

def polls_result(request, question_id):

    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'results.html', {'question': question})


# View for questions list
def polls_questions_list(request):

    data = Question.objects.all()
    print(data)

    context = {'title': 'Question List Page',
               'data':data}

    return render(request, 'questions-list.html', context)

