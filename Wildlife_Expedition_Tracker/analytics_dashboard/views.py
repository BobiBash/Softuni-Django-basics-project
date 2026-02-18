import base64

from django.db.models import Count
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
from sightings.models import Sighting
from expeditions.models import Expedition

# Create your views here.
def analytics_dashboard(request: HttpRequest) -> HttpResponse:
    top_animal = (Sighting
    .objects
    .values('animal__name')
    .annotate(animal_count=Count('animal__name'))
    .order_by('animal__name')
    .first())

    top_location = (Expedition
    .objects
    .values('location')
    .annotate(location_count=Count('location'))
    .order_by('location')
    .first())




    # fig, ax = plt.subplots(figsize=(6, 4))
    # ax.bar(value_one, value_two, align='center')
    # ax.set_yticks(np.arange(0, max(top_5_animal_count) + 1, step=1))
    # ax.set_title(title)
    # plt.tight_layout()
    #
    # buffer = BytesIO()
    # plt.savefig(buffer, format='png')
    # buffer.seek(0)
    # image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    # plt.close(fig)

    context = {'top_animal': top_animal, 'top_location': top_location}




    return render(request, 'analytics/analytics_dashboard.html', context)
