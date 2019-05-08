from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def polls_index(*args, **kwargs):
	return HttpResponse("<h1>Polls Index</h1>")