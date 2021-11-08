from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request,"index.html")


def output(request):
    return render(request,"output.html")


def compare(request):
    return render(request,"compare.html")

def test(request):
    return render(request,"test.html")

def test2(request):
    
    return render(request,"test2.html")
   

def videoupload(request):
    return render(request,"videoupload.html")

def  Builderapp(request):
    return render(request,"testForBuilderapp.html")

def  pannellum(request):
    return render(request,"pannellum.html")