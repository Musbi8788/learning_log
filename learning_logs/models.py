from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    """A topic the user in learning about."""
    text = models.CharField(max_length=200) # create a text topic database for the user
    author = models.CharField(max_length=200)
    data_added = models.DateTimeField(auto_now_add=True) # set the current time any time the user create a new topic
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) :
        """Return a string representating of the model."""
        return self.text
    

class Entry(models.Model):
    """Something specific learned about a topic."""
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    text = models.TextField()
    data_added = models.DateTimeField(auto_now_add=True)
    
    
    class Mete:
        verbose_name_plunal = 'entries'

    def __str__(self):
        """Return a string representation of the model."""
        Max_Char = 50
        if not self.text:
            return ""
        
        return self.text if len(self.text) <= Max_Char else f"{self.text[:Max_Char]}..."

        