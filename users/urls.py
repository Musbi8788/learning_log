# Define URL pattern for  users

from django.urls import path, include
from . import views 

app_name = "users"

urlpatterns = [
    # Include default auth urls
    path('',  include('django.contrib.auth.urls')), # render default django authentication urls eg login & logout.
    # Registration page
    path('register/', views.register, name='register'),
    path('users/logout/', views.logout_view, name='logout'),
]
