from django import forms

from .models import Sighting

class SightingForm(forms.ModelForm):

    class Meta:
        model = Sighting
        fields = ['expedition',
                  'animal',
                  'observed_at',
                  'count',
                  'latitude',
                  'longitude',
                  'notes',
                  'animal_image',
                  ]