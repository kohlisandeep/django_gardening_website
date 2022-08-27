from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html',{'name':'Sandeep'})
def add(request):
    v1=int(request.POST["num1"])
    v2=int(request.POST["num2"])
    v3=v1+v2
    return render(request,'result.html',{'result':v3})
