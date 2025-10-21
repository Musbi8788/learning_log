# Install Django

'''django-admin startproject learning_log .'''

The . dot makes it easy with deploying the project


## 
Don’t forget this dot, or you might run into some configuration issues when you
deploy the app. If you forget the dot, delete the files and folders that were created
(except ll_env), and run the command again

## Creating database

run python manage.py migrate to create the db or make some changes


## Creating apps 
'''python manage.py startapp learning_logs'''

## Creating superuser
'''python manage.py creatsuperuser'''

# Styling and Deloying the site
""
pip install django-bootstrap4
"""
We ignore the styling until now because we are focusing on the backend of the application. and styling is only important when you have a working application.