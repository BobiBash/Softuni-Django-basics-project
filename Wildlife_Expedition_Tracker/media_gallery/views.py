from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def display_gallery(request: HttpRequest) -> HttpResponse:
    pass

def image_detail(request: HttpRequest, slug: str) -> HttpResponse:
    pass