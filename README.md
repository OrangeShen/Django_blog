# Django_blog  
This is a learning progress of building a simple blog using Django 2.0.1, which is the newest version.  
  However, based on the gitbook 《Django搭建简易博客教程》https://github.com/Andrew-liu/my_blog_tutorial, which uses a old version of Django, I came across many problems, so I will list all the steps and try to update them in my code.  
  Feel free to check it out and put forword your questions.  
  My list of development enviroment:  
* macOS High Sierra 10.13.2  
* Python 3.6.4  
* Django 2.0.1  
* vs code 1.19.3  
* virtualenv 15.1.0  
## Day 1
### Create a Python virtual enviroment   
     $ virtualenv -p /usr/local/bin/python3 ENV3   
### Active virtual enviroment   
     $ source ENV3/bin/activate (no slash(/) at the begining of path since we didn't change directory)   
### Install git and tree   
     $ brew install git  
     $ brew install tree  
### Start a new project named 'my_blog'  
     $ django-admin.py startproject my_blog  
### Create a new app, don't forget to cd into your project folder before running manage.py  
     $ python manage.py startapp article  
     Then insert the app in setting.py, append in the INSTALLED_APPS dict.  
### Start a local server to test app  
     $ Python manage.py migrate  
     $ python manage.py runserver  
### Modify models.py, then run the following command in ENV3  
     $ python manage.py makemigrations  
     $ python manage.py migrate  
## Here is my urls.py  
<pre><code>  
from django.contrib import admin  
from django.urls import path, re_path  
from article import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', views.home),
    re_path(r'^(?P<my_args>\d+)/$', views.detail),
]
</code></pre>
  In the new version of Django, if you need to match urls using regex, you have to import the re_path method.  
### Create a superuser and register your app  
     $ python manage.py createsuperuser  
### I didn't manage to using the plugin bootstrap_admin because it raised exceptions that I don't know how to deal with.  
     
## Day 2  
  stay tuned...
