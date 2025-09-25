from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404


from .models import Entry, Topic
from .forms import TopicForm, EntryForm

# Create your views here.

def index(request):
    """The home page for Learning Log."""
    return render(request, "learning_logs/index.html")

@login_required
def topics(request):
    """Show all topics"""
    topics = Topic.objects.filter(owner=request.user).order_by('data_added') # sort the topics by date # make each user see only their own data.
    context = {'topics': topics}
    return render(request, "learning_logs/topics.html", context)

@login_required
def topic(request, topic_id):
    """Show a single topic and all it entries."""
    topic = Topic.objects.get(id=topic_id)
    # Make sure the topic belown to the user.
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-data_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, "learning_logs/topic.html", context)

@login_required
def new_topic(request):
    """Add a new topic."""
    if request.method != "POST":
        # No data submitted, create a blank form.
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST) # store the user info in topicform
        if form.is_valid(): # check if the form is valid
            # Associate topic ownership to users
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save() # save form
            return redirect("learning_logs:topics") # send the user back to topics page
    # Display a blank or invalid form
    context = {'form': form}
    return render(request, "learning_logs/new_topic.html", context)
@login_required
def new_entry(request, topic_id):
    """Add a new entry for a particular topic"""
    topic = Topic.objects.get(id=topic_id) # get the correct topic id
    if request.method != "POST":
        # No data submitted; create a blank form.
        form = EntryForm() # create an instand form
    else:
        # Post data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False) # store the entry without saving it yet to the database 
            new_entry.topic = topic # add the entry to the particular topic
            new_entry.save() # Save the entry to it associated topic
            return redirect("learning_logs:topic", topic_id=topic_id) # redirect user the exact topic url
        
    # Display a blank or invalid form.
    context = {'topic': topic, 'form': form}
    return render(request, "learning_logs/new_entry.html", context)

@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry"""
    entry = Entry.objects.get(id=entry_id) # get the topic entry user's what to edit
    topic = entry.topic 
    if topic.owner != request.user:
        raise Http404

    if request.method != "POST":
        # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry) 
    else:
        # Post data submitted; process data
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
        return redirect('learning_logs:topic', topic_id=topic.id)
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, "learning_logs/edit_entry.html", context)