from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.
def say_hello(request):
    # return HttpRequest('Hello World')
    return render(request, 'hello.html',{'name':'Mosh'})
