"""my_newblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, re_path
from article import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', views.home, name="home"),
    re_path(r'^(?P<id>\d+)/$', views.detail, name="detail"),
    re_path(r'^test/$', views.test, name="test"),
    re_path(r'^archives/$', views.archives, name="archives"),
    re_path(r'^aboutme/$', views.about_me, name="aboutme"),
    re_path(r'^tag(?P<tag>\w+)/$', views.search_tag, name="search_tag"),
    re_path(r'^search/$', views.blog_search, name="search"),
    re_path(r'^RSSFeed/$', views.RSSFeed(), name="RSS"),
]
