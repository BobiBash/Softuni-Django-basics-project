from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import AnimalForm
from .models import Animal

# Create your views here.
def animals_list(request: HttpRequest) -> HttpResponse:
    animals = Animal.objects.all()
    context = {
        "animals": animals
    }
    return render(request, "animals/animals_list.html", context)

def animal_detail(request: HttpRequest, slug: str) -> HttpResponse:
    animal = get_object_or_404(Animal, slug=slug)

    context = {
        'animal': animal
    }

    return render(request, "animals/animal_detail.html", context)

def add_animal(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = AnimalForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Animal Added Successfully")
            return redirect('animals_list')
        else:
            messages.error(request, "Please correct the error/s below.")
    else:
        form = AnimalForm()

    context = {
        "form": form,
        "title": "Add Animal",
    }

    return render(request, "animals/add_animal.html", context)