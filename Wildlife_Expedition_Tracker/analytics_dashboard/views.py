import base64
import datetime as dt

import calendar as cal

from charset_normalizer import md
from django.db.models import Count, Avg
from django.db.models.functions import TruncDate, TruncMonth
from django.forms import model_to_dict
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
import matplotlib
from matplotlib.dates import DayLocator, DateFormatter

matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
from sightings.models import Sighting
from expeditions.models import Expedition

# Create your views here.
def analytics_dashboard(request: HttpRequest) -> HttpResponse:

    top_animals = (Sighting
    .objects
    .values('animal__name')
    .annotate(animal_count=Count('animal__name'))
    .order_by('-animal_count')[:5])

    top_locations = (Expedition
    .objects
    .values('location')
    .annotate(location_count=Count('location'))
    .order_by('-location_count')[:5])

    top_animals = top_animals.values('animal__name', 'animal_count')
    top_locations = top_locations.values('location', 'location_count')
    print(top_locations)

    today = dt.date.today()
    first_day = today.replace(day=1)
    last_day = today.replace(day=cal.monthrange(today.year, today.month)[1])

    data = Sighting.objects.filter(
        observed_at_date__year=today.year,
        observed_at_date__month=today.month - 1
    ).values('observed_at_date').annotate(
        avg_animals=Avg('count')
    ).order_by('observed_at_date')

    last_month = dt.datetime.now().month - 1
    current_year = dt.datetime.now().year
    num_days = cal.monthrange(current_year, last_month)[1]

    print(num_days)
    days = [dt.date(current_year, last_month, day) for day in range(1, num_days + 1)]

    data_dict = {d['observed_at_date']: d['avg_animals'] for d in data}

    labels = [''] * len(days)
    labels[0] = first_day.strftime('%d %b')
    labels[-1] = last_day.strftime('%d %b')
    values = [data_dict.get(day, 0) for day in days]

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.tick_params(axis='x', labelsize=18)
    ax.tick_params(axis='y', labelsize=18)
    ax.plot(days, values, marker='None', linewidth=1, color='steelblue')
    plt.title("Average monthly expeditions (last month)", fontsize=18)
    ax.set_yticks(range(0, int(max(values)) + 2, 1))
    ax.margins(x=0.02)
    interval = 5
    tick_days = [days[0]] + days[interval::interval] + [days[-1]]
    ax.set_xticks(tick_days)
    ax.xaxis.set_major_formatter(DateFormatter('%d %b'))
    plt.tight_layout()

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    plt.close(fig)

    context = {'top_animals': top_animals,
               'top_locations': top_locations,
               'chart': image_base64}




    return render(request, 'analytics/analytics_dashboard.html', context)
