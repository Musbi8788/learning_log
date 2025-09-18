from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm # import default django registration form

# Create your views here.
def register(request):
    """Register a new user"""
    if request.method != "POST":
        # Display a blank registration form
        form = UserCreationForm() # generate default registratoin 
    else:
        # Process completed form.
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # Log the user in then redirect to home page
            login(request, new_user) # login the user after the created an account.
            return redirect('learning_logs:index')

    # Display a blank or invalid form
    context = {'form': form }
    return render(request, "registration/register.html", context)