import base64
import datetime as dt

import calendar as cal
import json

from django.db.models import Count, Avg
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

    today = dt.date.today()

    if today.month == 1:
        last_month_num = 12
        last_month_year = today.year - 1
    else:
        last_month_num = today.month - 1
        last_month_year = today.year

    data = Sighting.objects.filter(
        observed_at_date__year=last_month_year,
        observed_at_date__month=last_month_num
    ).values('observed_at_date').annotate(
        avg_animals=Avg('count')
    ).order_by('observed_at_date')

    num_days = cal.monthrange(last_month_year, last_month_num)[1]

    days = [dt.date(last_month_year, last_month_num, day) for day in range(1, num_days + 1)]

    data_dict = {d['observed_at_date']: float(d['avg_animals']) for d in data}
    print(data_dict)

    values = [data_dict.get(day, 0) for day in days]
    labels = [d.strftime('%d %b') for d in days]



    context = {'top_animals': top_animals,
               'top_locations': top_locations,
               'chart_labels': json.dumps(labels),
               'chart_values': json.dumps(values),
               'chart_month': cal.month_name[last_month_num]}


    return render(request, 'analytics/analytics_dashboard.html', context)
