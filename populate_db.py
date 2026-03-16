import os
import django
import random
from datetime import datetime, timedelta, time

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Wildlife_Expedition_Tracker.settings")
django.setup()

from animals.models import Animal
from expeditions.models import Expedition
from sightings.models import Sighting


def create_animals():
    animals = []
    animal_names = [
        "African Elephant",
        "Lion",
        "Giraffe",
        "Zebra",
        "Cheetah",
        "Hippopotamus",
        "Rhinoceros",
        "Leopard",
        "African Buffalo",
        "Wildebeest",
        "Spotted Hyena",
        "African Wild Dog",
        "Impala",
        "Gazelle",
        "Baboon",
        "Crocodile",
        "Flamingo",
        "Ostrich",
        "Meerkat",
        "Warthog",
        "Serval",
    ]

    for i in range(21):
        name = animal_names[i % len(animal_names)]
        animal, created = Animal.objects.get_or_create(
            name=f"{name} {i + 1}",
            defaults={
                "kingdom": "Animalia",
                "group": "Mammal",
                "food": "Herbivore",
                "most_distinctive_feature": "Test feature",
                "weight": "100-200 kg",
            },
        )
        animals.append(animal)
        print(f"Created animal: {animal.name}")

    return animals


def create_expeditions(animals):
    expeditions = []
    locations = [
        "Serengeti National Park, Tanzania",
        "Kruger National Park, South Africa",
        "Maasai Mara, Kenya",
        "Okavango Delta, Botswana",
        "Bwindi Impenetrable Forest, Uganda",
        "Namib Desert, Namibia",
        "Lake Nakuru, Kenya",
        "Hwange National Park, Zimbabwe",
        "Zambezi River, Zambia",
        "Nyungwe Forest, Rwanda",
        "iSimangaliso Wetland Park, South Africa",
        "Amboseli National Park, Kenya",
        "Etosha National Park, Namibia",
        "Lewa Wildlife Conservancy, Kenya",
        "Kgalagadi Transfrontier Park, Botswana",
        "Ngorongoro Crater, Tanzania",
        "Virunga National Park, DRC",
        "South Luangwa National Park, Zambia",
        "Selous Game Reserve, Tanzania",
        "Moremi Game Reserve, Botswana",
        "Kibale Forest, Uganda",
    ]

    for i in range(21):
        expedition, created = Expedition.objects.get_or_create(
            title=f"Expedition {i + 1}",
            defaults={
                "target_species": animals[i % len(animals)],
                "description": f"Description for expedition {i + 1}",
                "location": locations[i % len(locations)],
                "start_date": datetime(2025, 1, 1) + timedelta(days=i * 30),
                "end_date": datetime(2025, 1, 10) + timedelta(days=i * 30),
            },
        )
        expeditions.append(expedition)
        print(f"Created expedition: {expedition.title}")

    return expeditions


def create_sightings(expeditions, animals):
    sightings = []

    for i in range(21):
        sighting = Sighting.objects.create(
            expedition=expeditions[i % len(expeditions)],
            animal=animals[i % len(animals)],
            observed_at_date=expeditions[i % len(expeditions)].start_date
            + timedelta(days=random.randint(0, 5)),
            observed_at_time=time(
                hour=random.randint(6, 18), minute=random.randint(0, 59)
            ),
            count=random.randint(1, 10),
            latitude=-1.2921 + random.uniform(-0.5, 0.5),
            longitude=36.8219 + random.uniform(-0.5, 0.5),
            notes=f"Sighting notes {i + 1}",
        )
        sightings.append(sighting)
        print(
            f"Created sighting: {sighting.animal.name} on {sighting.observed_at_date}"
        )

    return sightings


def main():
    print("Starting database population...")

    print("\n=== Creating Animals ===")
    animals = create_animals()

    print("\n=== Creating Expeditions ===")
    expeditions = create_expeditions(animals)

    print("\n=== Creating Sightings ===")
    sightings = create_sightings(expeditions, animals)

    print(f"\n=== Population Complete ===")
    print(f"Created {len(animals)} animals")
    print(f"Created {len(expeditions)} expeditions")
    print(f"Created {len(sightings)} sightings")


if __name__ == "__main__":
    main()
