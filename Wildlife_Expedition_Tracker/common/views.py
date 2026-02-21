from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.utils.text import slugify

from sightings.models import Sighting
from animals.models import Animal

from .forms import SearchForm


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

def search_view(request:HttpRequest) -> HttpResponse:
    form = SearchForm(request.GET or None)
    results = []
    print(form)

    if form.is_valid():
        print("form is valid")
        query = form.cleaned_data.get('query')
        print(query)
        if query:
            results = Animal.objects.filter(name__icontains=query)
        return redirect(f'animals/{slugify(query)}')

    context = {
        'form': form,
        'results': results
    }

    return render(request, 'common/home.html', context)