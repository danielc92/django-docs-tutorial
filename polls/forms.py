from .models import Poll
from django import forms

class PollForm(forms.ModelForm):
    
    c1 = forms.CharField(help_text="At least two choices are required.", label = "Choice 1", max_length=255)
    c2 = forms.CharField(help_text="At least two choices are required.", label = "Choice 2", max_length=255)
    c3 = forms.CharField(label = "Choice 3", max_length=255, required=False)
    c4 = forms.CharField(label = "Choice 4", max_length=255, required=False)

    class Meta:
        model = Poll
        fields = ['title', 'tags', 'author']