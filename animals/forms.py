from django import forms
from .models import Animal


class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = [
            "name",
            "kingdom",
            "group",
            "food",
            "most_distinctive_feature",
            "weight",
        ]

        help_texts = {
            "name": "Name",
            "kingdom": "Kingdom",
            "group": "Group",
            "food": "Food",
            "most_distinctive_feature": "Most Distinctive Feature",
            "weight": "Weight",
        }

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "border rounded-sm p-2 w-full bg-white",
                    "placeholder": "Enter animal name",
                }
            ),
            "kingdom": forms.TextInput(
                attrs={
                    "class": "border rounded-sm p-2 w-full bg-white",
                    "placeholder": "e.g., Animalia",
                }
            ),
            "group": forms.TextInput(
                attrs={
                    "class": "border rounded-sm p-2 w-full bg-white",
                    "placeholder": "e.g., Mammal",
                }
            ),
            "food": forms.TextInput(
                attrs={
                    "class": "border rounded-sm p-2 w-full bg-white",
                    "placeholder": "e.g., Carnivore",
                }
            ),
            "most_distinctive_feature": forms.TextInput(
                attrs={
                    "class": "border rounded-sm p-2 w-full bg-white",
                    "placeholder": "e.g., Long trunk",
                }
            ),
            "weight": forms.TextInput(
                attrs={
                    "class": "border rounded-sm p-2 w-full bg-white",
                    "placeholder": "e.g., 5000 kg",
                }
            ),
        }


class DeleteAnimalForm(AnimalForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.disabled = True
            field.read_only = True
