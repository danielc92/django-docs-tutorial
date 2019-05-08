from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Choice


# View for questions list
def polls_questions_list(request):

	data = Question.objects.all()
	print(data)

	context = {'title': 'Question List Page',
			   'data':data}

	return render(request, 'questions-list.html', context)