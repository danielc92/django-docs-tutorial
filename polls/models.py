from django.db import models

# Create your models here.
class Question(models.Model):

    choices = (
        ('POL', 'Politics'),
        ('SCI', 'Science'),
        ('FOO', 'Food'),
        ('TEC', 'Technology'),
        ('FAS', 'Fashion'),
        ('ADV', 'Advice'),
        ('OTH', 'Other')
    )   

    question_text = models.CharField(max_length=200)
    category = models.CharField(max_length=3,
                                choices=choices,
                                default='OTH')
    author = models.CharField(max_length=60, default='Anonymous')
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text