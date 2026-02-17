from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from sightings.models import Sighting


# Create your views here.
def home(request: HttpRequest) -> HttpResponse:
    return render(request, "common/home.html")

def about(request: HttpRequest) -> HttpResponse:
    pass

def media_gallery(request: HttpRequest) -> HttpResponse:

    sighting_images = Sighting.objects.exclude(animal_image=None).exclude(animal_image='')
    print(sighting_images)

    context = {
        'sighting_images': sighting_images
    }

    return render(request, 'common/image_gallery.html', context)