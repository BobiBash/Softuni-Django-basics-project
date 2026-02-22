from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .forms import SightingForm, SightingDeletingForm
from .models import Sighting
from expeditions.models import Expedition


# Create your views here.

def sighting_list(request: HttpRequest, slug: str) -> HttpResponse:
    expedition = get_object_or_404(Expedition, slug=slug)
    sightings = Sighting.objects.filter(expedition=expedition).order_by('-observed_at_date')

    context = {
        'expedition': expedition,
        'sightings': sightings
    }

    return render(request, 'sightings/sighting_list.html', context)

def sighting_detail(request: HttpRequest, slug: str, pk: int) -> HttpResponse:
    expedition = get_object_or_404(Expedition, slug=slug)
    sighting = get_object_or_404(Sighting, expedition=expedition, pk=pk)

    context = {
        'sighting': sighting,
    }

    return render(request, 'sightings/sighting_detail.html', context)

def add_sighting(request: HttpRequest, slug: str) -> HttpResponse:
    expedition = get_object_or_404(Expedition, slug=slug)

    form = SightingForm(request.POST, request.FILES)

    if request.method == 'POST':

        form = SightingForm(request.POST, request.FILES)

        if form.is_valid():

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
        'form': form,
        'sighting': sighting
    }

    return render(request, 'sightings/edit_sighting.html', context)

def delete_sighting(request: HttpRequest, slug: str, pk: int) -> HttpResponse:
    expedition = get_object_or_404(Expedition, slug=slug)
    sighting = get_object_or_404(Sighting, expedition=expedition, pk=pk)

    if request.method == 'POST':
        form = SightingDeletingForm(request.POST, request.FILES, instance=sighting)
        if form.is_valid():
            sighting.delete()
            return redirect('sighting_list', slug=slug)

    form = SightingDeletingForm()

    context = {
        'sighting': sighting,
        'form': form
    }

    return render(request, 'sightings/delete_sighting.html', context)

