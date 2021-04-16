from django.shortcuts import render
import os
from django.http import HttpResponse


# Create your views here.

def if_demo(request):
    login=True
    return render(request,'if_demo.html',context={'login':login})

def ifelse_demo(request):
    login=True
    return render(request,'ifelse_demo.html',context={'login':'login','name':'karthi','a':10,'b':45})

def for_demo(request):
    return render(request,'for_demo.html',{'items':['apple','ball','cat'],'profile':{'name':'karthi','age':25,'sal':10}})
