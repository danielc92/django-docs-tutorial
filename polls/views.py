from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def detail(request, question_id):
	return HttpResponse("You're looking at question {}"\
		.format(question_id))

def results(request, question_id):
	return HttpResponse("Your're looking at the results of question {}"\
		.format(question_id))

def vote(request, question_id):
	return HttpResponse("You're voting on question {}"\
		.format(question_id))