from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'myApp/index.html')
    # return HttpResponse('Hello World')


def about(request):
    return render(request, 'myApp/about.html')
