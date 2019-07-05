from django.db import models

# Create your models here.
class Tag(models.Model):

    tag_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tag_name


class Poll(models.Model):

    title = models.CharField(max_length=50, unique=True)
    tags = models.ManyToManyField(Tag)
    author = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Option(models.Model):
    
    text = models.CharField(max_length=255)
    poll = models.ForeignKey(Poll, related_name='options', on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.text} - {self.poll}"
