from django.http import HttpResponse
from django.shortcuts import render


def index(requext):
    return HttpResponse('Shivani New account')


def new(request):
    return HttpResponse('Open the account')




