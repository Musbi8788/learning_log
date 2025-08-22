"""Defines URL pattern for learning_logs """

from os import name
from django.urls import path
from . import views # import all the route comming for views.py

app_name = 'learning_logs'

urlpattern = [
    # Home page
    path('', views.index, name='index')
]
