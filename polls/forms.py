from django import forms
from .models import Question, Choice

class RawQuestionForm(forms.Form):
	question_text = forms.CharField()
	category = forms.ChoiceField(choices=(
        ('POL', 'Politics'),
        ('SCI', 'Science'),
        ('FOO', 'Food'),
        ('TEC', 'Technology'),
        ('FAS', 'Fashion'),
        ('ADV', 'Advice'),
        ('OTH', 'Other')
    )  )
	author = forms.CharField()

class RawChoiceForm(forms.Form):
	choice_text = forms.CharField()