from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from django.utils.text import slugify

from .forms import ExpeditionForm, ExpeditionDeleteForm
from .models import Expedition
from sightings.models import Sighting


# Create your views here.
def add_expedition(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ExpeditionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Expedition Added Successfully")
            return redirect('expeditions_list')
        else:
            messages.error(request, "Please correct the error/s below.")

    else:
        form = ExpeditionForm()

    context = {
        "form": form,
        "title": "Add Expedition",
    }

    return render(request, "expeditions/add_expedition.html", context)

def expedition_detail(request: HttpRequest, slug: str) -> HttpResponse:
    expedition = get_object_or_404(Expedition, slug=slug)

    context = {
        "expedition": expedition,
    }

    return render(request, "expeditions/expedition_detail.html", context)

def expeditions_list(request: HttpRequest) -> HttpResponse:
    expeditions = Expedition.objects.all().order_by("title")

    paginator = Paginator(expeditions, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }
    return render(request, "expeditions/expeditions_list.html", context)

def edit_expedition(request: HttpRequest, slug: str) -> HttpResponse:
    expedition = get_object_or_404(Expedition, slug=slug)

    if request.method == "POST":
        form = ExpeditionForm(request.POST, instance=expedition)
        if form.is_valid():
            expedition = form.save(commit=False)
            if 'title' in form.changed_data:
                base_slug = slugify(expedition.title)
                expedition.slug = expedition._generate_unique_slug(base_slug)
            expedition.save()
            return redirect('expeditions_list')
    else:
        form = ExpeditionForm(instance=expedition)

    context = {
        "expedition": expedition,
        "form": form,
    }
    return render(request, "expeditions/edit_expedition.html", context)

def delete_expedition(request: HttpRequest, slug: str) -> HttpResponse:
    expedition = get_object_or_404(Expedition, slug=slug)
    form = ExpeditionDeleteForm(instance=expedition)

    if request.method == "POST":
        expedition.delete()
        return redirect('expeditions_list')

    context = {
        "expedition": expedition,
        "form": form
    }

    return render(request, 'expeditions/expeditions_confirm_delete.html', context)

