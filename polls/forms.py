from django import forms
from .models import Question, Choice, choices

class RawQuestionForm(forms.ModelForm):
	question_text = forms.CharField()
	category = forms.ChoiceField(choices=choices)
	author = forms.CharField()

class RawChoiceForm(forms.Form):
	choice_text = forms.CharField()