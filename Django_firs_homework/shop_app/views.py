from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def shop_list(request):
    return HttpResponse("Hello, world. You're at the polls list.")
