from django.contrib import admin
from django.urls import path
from polls.views import polls_list, option_vote, polls_view, polls_index, polls_create
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', polls_index, name='polls-index'),
    path('polls/list/', polls_list, name='polls-list'),
    path('polls/create/', polls_create , name='polls-create'),
        path('vote/<int:option_id>/', option_vote, name='polls-vote'),
    path('polls/view/<int:poll_id>/', polls_view, name='polls-view')
    ]
    
urlpatterns += staticfiles_urlpatterns()
