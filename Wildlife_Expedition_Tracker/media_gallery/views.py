from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import MediaGallery


# Create your views here.
def display_gallery(request: HttpRequest) -> HttpResponse:
    gallery_photos = MediaGallery.objects.all()

    context = {
        "photos": gallery_photos
    }

    return render(request, "media_gallery.html", context)

def image_detail(request: HttpRequest, slug: str) -> HttpResponse:
    pass