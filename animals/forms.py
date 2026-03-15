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

        error_messages = {
            'name': {
                'required': 'Animal name is a required field.',
                'max_length': 'Cannot exceed 100 characters.',
            },
            'kingdom': {
                'required': 'Animal kingdom is a required field.',
                'max_length': 'Cannot exceed 50 characters.',
            },
            'group': {
                'required': 'Animal group is a required field.',
                'max_length': 'Cannot exceed 50 characters.',
            },
            'food': {
                'required': 'Animal food is a required field.',
                'max_length': 'Cannot exceed 100 characters.',
            },
            'most_distinctive_feature': {
                'required': 'Animal most distinctive feature is a required field.',
                'max_length': 'Cannot exceed 150 characters.',
            },
            'weight': {
                'required': 'Animal weight is a required field.',
                'max_length': 'Cannot exceed 50 characters.',
            },
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
