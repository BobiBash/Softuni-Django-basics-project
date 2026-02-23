from datetime import timedelta

from django import template
from django.utils import timezone
from expeditions.models import Expedition
from sightings.models import Sighting
from animals.models import Animal

register = template.Library()

@register.simple_tag(name='total_expeditions')
def total_expeditions():
    return Expedition.objects.all().count()

@register.simple_tag(name='total_sightings')
def total_sightings():
    return Sighting.objects.all().count()

@register.simple_tag(name='recent_expedition')
def recent_expedition():
    return Expedition.objects.all().order_by('-created_at').first()

@register.simple_tag(name='recent_sighting')
def recent_sighting():
    return Sighting.objects.all().order_by('-created_at').first()

@register.simple_tag(name='random_animal_fact')
def random_animal_fact():
    facts = Animal.objects.values('name', 'most_distinctive_feature')
    if facts:
        import random
        print(random.choice(facts))
        return random.choice(facts)
    return "No animal facts available."

@register.filter(name='is_new')
def is_new(value):
    return timezone.now() - value < timedelta(hours=24)