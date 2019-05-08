from django import forms
from .models import Question, Choice

class RawQuestionForm(forms.Form):
	question_text = forms.CharField()

class RawChoiceForm(forms.Form):
	choice_text = forms.CharField()