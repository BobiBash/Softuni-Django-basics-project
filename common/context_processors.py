from animals.models import Animal
from expeditions.models import Expedition

def search_data(request):
    return {
        'animals': Animal.objects.all().only('name'),
        'expeditions': Expedition.objects.all().only('title'),
    }