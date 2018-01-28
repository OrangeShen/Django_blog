from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article

# Create your views here.
def home(request):
    return HttpResponse("hello django!")

def detail(request, my_args):
    post = Article.objects.all()[int(my_args)]
    str = ("title = {0}, category = {1}, date_time = {2}, content = {3}".format(post.title, post.category, post.category, post.content))
    return HttpResponse(str)