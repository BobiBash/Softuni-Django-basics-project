from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.utils.text import slugify

from expeditions.models import Expedition
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
            # Search in animal model
            animal_results = Animal.objects.filter(name__icontains=query)

            # Search in expedition model
            expedition_results = Expedition.objects.filter(title__icontains=query)

            results = [
                *[{'type': 'Animal', 'name': a.name, 'url': a.get_absolute_url()} for a in animal_results],
                *[{'type': 'Expedition', 'name': e.title, 'url': e.get_absolute_url()} for e in expedition_results],
            ]

    context = {
        'form': form,
        'results': results,
        'query': request.GET.get('query', '')
    }

    return render(request, 'common/search.html', context)