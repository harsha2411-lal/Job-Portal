from django.shortcuts import render


def job(req):
    return render(req,'ex1.html')

def signin(req):
    return render(req,'sign.html')

def register(req):
    return render(req,'register.html')
# Create your views here.

