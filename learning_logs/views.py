from django.shortcuts import render, redirect

from .models import Topic
from .forms import TopicForm

# Create your views here.

def index(request):
    """The home page for Learning Log."""
    return render(request, "learning_logs/index.html")

def topics(request):
    """Show all topics"""
    topics = Topic.objects.order_by('data_added')
    context = {'topics': topics}
    return render(request, "learning_logs/topics.html", context)

def topic(request, topic_id):
    """Show a single topic and all it entries."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-data_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, "learning_logs/topic.html", context)

def new_topic(request):
    """Add a new topic."""
    if request.method != "POST":
        # No data submitted, create a blank form.
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST) # store the user info in topicform
        if form.is_valid(): # check if the form is valid
            form.save() # save form
            return redirect("learning_logs:topics") # send the user back to topics page
    # Display a blank or invalid form
    context = {'form': form}
    return render(request, "learning_logs/new_topic.html", context)
