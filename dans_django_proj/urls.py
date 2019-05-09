"""dans_django_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from polls.views import polls_questions_list, polls_create_choice, polls_vote, polls_result, polls_index, polls_create_question
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', polls_index, name='polls-index'),
    path('polls/list/', polls_questions_list, name='polls-list'),
    path('polls/vote/<int:question_id>/', polls_vote, name='polls-vote'),
    path('polls/results/<int:question_id>/', polls_result, name='polls-results'),
    path('polls/create-question/', polls_create_question, name='polls-create-question'),
    path('polls/create-choice/<int:question_id>/', polls_create_choice, name='polls-create-choice'),
    path('admin/', admin.site.urls)
    ]
    
urlpatterns += staticfiles_urlpatterns()
