from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<h1> You are in index of APP1</h1>")

def sample1(request):
    return render(request,'sample.html')

