from django.shortcuts import render, HttpResponse
# Create your views here.

def hello(request,nome,idade):
    return HttpResponse('<h1>Hello {}</h1>'.format(nome,idade))