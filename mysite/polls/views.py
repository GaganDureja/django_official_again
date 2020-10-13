from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
	request HttpResponse('Hello, world. You\' st the polls index.')
