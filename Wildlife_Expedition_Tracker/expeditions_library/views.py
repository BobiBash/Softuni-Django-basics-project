from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.

def display_expeditions(request: HttpRequest) -> HttpResponse:
    pass

def edit_expedition(request: HttpRequest, pk: int) -> HttpResponse:
    pass

def delete_expedition(request: HttpRequest, pk: int) -> HttpResponse:
    pass