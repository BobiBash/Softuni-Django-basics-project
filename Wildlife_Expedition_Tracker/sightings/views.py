from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .forms import SightingForm
from .models import Sighting
from expeditions.models import Expedition


# Create your views here.

def sighting_list(request: HttpRequest, slug) -> HttpResponse:
    expedition = get_object_or_404(Expedition, slug=slug)
    sightings = Sighting.objects.filter(expedition=expedition).order_by('-observed_at')

    context = {
        'expedition': expedition,
        'sightings': sightings
    }

    return render(request, 'sightings/sighting_list.html', context)

def sighting_detail(request: HttpRequest, slug: str) -> HttpResponse:
    ...

def add_sighting(request: HttpRequest, slug: str) -> HttpResponse:
    expedition = get_object_or_404(Expedition, slug=slug)

    if request.method == 'POST':
        print("post request received")
        form = SightingForm(request.POST, request.FILES)
        print(f"{request.POST}")
        if form.is_valid():
            print("form is valid")
            sighting = form.save(commit=False)
            sighting.expedition = expedition
            sighting.save()
            return redirect('sighting_list', slug=slug)
    else:
        form = SightingForm()

    context = {
        'expedition': expedition,
        'form': form
    }

    return render(request, 'sightings/add_sighting.html', context)



def edit_sighting(request: HttpRequest, slug: str, pk: int) -> HttpResponse:
    expedition = get_object_or_404(Expedition, slug=slug)
    sighting = get_object_or_404(Sighting, expedition=expedition, pk=pk)

    if request.method == 'POST':
        form = SightingForm(request.POST, request.FILES, instance=sighting)
        if form.is_valid():
            sighting.save()
            return redirect('sighting_list', slug=slug)

    form = SightingForm(instance=sighting)

    context = {
        'form': form
    }

    return render(request, 'sightings/edit_sighting.html', context)

def delete_sighting(request: HttpRequest, slug: str) -> HttpResponse:
    ...