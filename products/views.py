from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('Cutie')


def new(request):
    return HttpResponse("New products")


