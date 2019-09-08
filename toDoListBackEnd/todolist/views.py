from django.shortcuts import render
from django.http import HttpResponse

# test route
def index(request):
    return HttpResponse("This is the index!")
# Create your views here.

# 