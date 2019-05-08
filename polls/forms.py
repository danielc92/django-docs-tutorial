from django import forms
from .models import Question, Choice

class RawQuestionForm(forms.Form):
	question_text = forms.CharField()

