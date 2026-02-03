from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .forms import AddExpeditionForm
from .models import Expedition


# Create your views here.
def add_expedition(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = AddExpeditionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Expedition Added Successfully")
        else:
            messages.error(request, "Please correct the error/s below.")

    else:
        form = AddExpeditionForm()

    context = {
        "form": form,
        "title": "Add Expedition",
    }

    return render(request, "expeditions/add_expedition.html", context)
def expedition_detail(request: HttpRequest, pk: int) -> HttpResponse:
    ...

def expeditions_list(request: HttpRequest) -> HttpResponse:
    expeditions = Expedition.objects.all()
    context = {
        "expeditions": expeditions
    }
    return render(request, "expeditions/expeditions_list.html", context)

def edit_expedition(request: HttpRequest, pk: int) -> HttpResponse:
    pass

def delete_expedition(request: HttpRequest, pk: int) -> HttpResponse:
    pass
