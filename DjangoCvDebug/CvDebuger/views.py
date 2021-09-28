from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request,"index.html")


def output(request):
    return render(request,"output.html")


def compare(request):
    return render(request,"compare.html")