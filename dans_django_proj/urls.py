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
from polls.views import polls_index, polls_detail, polls_results, polls_vote

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/details/<int:question_id>/', polls_detail, name='polls_detail'),
    path('polls/results/<int:question_id>/', polls_detail, name='polls_results'),
    path('polls/vote/<int:question_id>/', polls_detail, name='polls_vote'),
    path('polls/', polls_detail, name='polls_index')
]
