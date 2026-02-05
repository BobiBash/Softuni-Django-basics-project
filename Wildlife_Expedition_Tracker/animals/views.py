from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Animal

# Create your views here.
def animals_list(request: HttpRequest) -> HttpResponse:
    animals = Animal.objects.all()
    context = {
        "animals": animals
    }
    return render(request, "animals/animals_list.html", context)