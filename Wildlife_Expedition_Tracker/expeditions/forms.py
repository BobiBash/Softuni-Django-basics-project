from django import forms

from .models import Expedition


class AddExpeditionForm(forms.ModelForm):
    class Meta:
        model = Expedition
        fields = ['title',
                  'primary_animal',
                  'additional_animals',
                  'description',
                  'location',
                  'animal_image']
        widgets = {
            'location': forms.CheckboxSelectMultiple(),
        }