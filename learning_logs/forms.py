from dataclasses import field
from django import forms # Import Form model

from .models import  Topic, Entry # Import Topic & Entry database from models.py

class TopicForm(forms.ModelForm):
    """A class handling the TopicForm"""
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': 'Entry:'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}