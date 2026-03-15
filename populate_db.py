import os

import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Wildlife_Expedition_Tracker.settings')
django.setup()


from animals.models import Animal


animals_data = [
    {
        "name": "African Elephant",
        "kingdom": "Animalia",
        "group": "Mammal",
        "food": "Grasses, leaves, bark, fruits",
        "most_distinctive_feature": "Large ears and long trunk",
        "weight": "4,000-7,000 kg"
    },
    {
        "name": "Bengal Tiger",
        "kingdom": "Animalia",
        "group": "Mammal",
        "food": "Deer, wild boar, buffalo",
        "most_distinctive_feature": "Orange coat with black stripes",
        "weight": "180-260 kg"
    },
    {
        "name": "Blue Whale",
        "kingdom": "Animalia",
        "group": "Mammal",
        "food": "Krill, small fish",
        "most_distinctive_feature": "Largest animal on Earth",
        "weight": "100,000-200,000 kg"
    },
    {
        "name": "Bald Eagle",
        "kingdom": "Animalia",
        "group": "Bird",
        "food": "Fish, small mammals, carrion",
        "most_distinctive_feature": "White head and yellow beak",
        "weight": "3-6.3 kg"
    },
    {
        "name": "Emperor Penguin",
        "kingdom": "Animalia",
        "group": "Bird",
        "food": "Fish, squid, krill",
        "most_distinctive_feature": "Largest penguin species",
        "weight": "22-45 kg"
    },
    {
        "name": "Giant Panda",
        "kingdom": "Animalia",
        "group": "Mammal",
        "food": "Bamboo shoots and leaves",
        "most_distinctive_feature": "Black and white fur pattern",
        "weight": "70-120 kg"
    },
    {
        "name": "Saltwater Crocodile",
        "kingdom": "Animalia",
        "group": "Reptile",
        "food": "Fish, birds, mammals",
        "most_distinctive_feature": "Largest living reptile",
        "weight": "400-1,000 kg"
    },
    {
        "name": "Great White Shark",
        "kingdom": "Animalia",
        "group": "Fish",
        "food": "Seals, sea lions, fish",
        "most_distinctive_feature": "Powerful jaws with rows of teeth",
        "weight": "680-1,100 kg"
    },
    {
        "name": "Mountain Gorilla",
        "kingdom": "Animalia",
        "group": "Mammal",
        "food": "Leaves, shoots, stems, bamboo",
        "most_distinctive_feature": "Thick black fur and large size",
        "weight": "140-200 kg"
    },
    {
        "name": "Polar Bear",
        "kingdom": "Animalia",
        "group": "Mammal",
        "food": "Seals, fish, walrus",
        "most_distinctive_feature": "White fur and adapted to cold",
        "weight": "350-700 kg"
    },
    {
        "name": "Red Fox",
        "kingdom": "Animalia",
        "group": "Mammal",
        "food": "Small rodents, rabbits, birds",
        "most_distinctive_feature": "Reddish-orange fur and bushy tail",
        "weight": "4-8 kg"
    },
    {
        "name": "Komodo Dragon",
        "kingdom": "Animalia",
        "group": "Reptile",
        "food": "Deer, pigs, smaller dragons",
        "most_distinctive_feature": "Largest living lizard",
        "weight": "70-90 kg"
    },
    {
        "name": "African Lion",
        "kingdom": "Animalia",
        "group": "Mammal",
        "food": "Zebras, wildebeest, buffalo",
        "most_distinctive_feature": "Male's distinctive mane",
        "weight": "120-190 kg"
    },
    {
        "name": "Snow Leopard",
        "kingdom": "Animalia",
        "group": "Mammal",
        "food": "Mountain goats, sheep, marmots",
        "most_distinctive_feature": "Thick spotted fur and long tail",
        "weight": "25-55 kg"
    },
    {
        "name": "Humpback Whale",
        "kingdom": "Animalia",
        "group": "Mammal",
        "food": "Krill, small fish",
        "most_distinctive_feature": "Long pectoral fins and singing",
        "weight": "25,000-30,000 kg"
    },
    {
        "name": "Grey Wolf",
        "kingdom": "Animalia",
        "group": "Mammal",
        "food": "Deer, elk, moose, smaller mammals",
        "most_distinctive_feature": "Pack behavior and howling",
        "weight": "30-80 kg"
    },
    {
        "name": "Cheetah",
        "kingdom": "Animalia",
        "group": "Mammal",
        "food": "Gazelles, impalas, small antelopes",
        "most_distinctive_feature": "Fastest land animal",
        "weight": "40-65 kg"
    },
    {
        "name": "Orangutan",
        "kingdom": "Animalia",
        "group": "Mammal",
        "food": "Fruits, leaves, insects",
        "most_distinctive_feature": "Long arms and reddish-brown hair",
        "weight": "30-90 kg"
    },
    {
        "name": "Green Sea Turtle",
        "kingdom": "Animalia",
        "group": "Reptile",
        "food": "Seagrass, algae, jellyfish",
        "most_distinctive_feature": "Heart-shaped shell",
        "weight": "150-200 kg"
    },
    {
        "name": "Grizzly Bear",
        "kingdom": "Animalia",
        "group": "Mammal",
        "food": "Fish, berries, roots, small mammals",
        "most_distinctive_feature": "Shoulder hump and large size",
        "weight": "180-360 kg"
    }
]

for animal in animals_data:
    Animal.objects.create(**animal)

print(f"Created {len(animals_data)} animals")