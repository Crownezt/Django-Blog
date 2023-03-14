from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def hello(request):
    return HttpResponse("Cohort 13")


def greet(request):
    return HttpResponse("Welcome to Django class")


def welcome(request):
    return render(request, 'post/welcome.html')


def comment(request):
    return render(request, 'post/comment.html')
