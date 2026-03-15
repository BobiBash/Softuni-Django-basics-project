from django import forms
from django.core.exceptions import ValidationError

from .models import Sighting

class SightingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['animal'].empty_label = 'Choose an animal'

    def clean_latitude(self):
        value = self.cleaned_data.get('latitude')
        if not value:
            return value
        try:
            value = float(value)
        except (ValueError, TypeError):
            raise ValidationError('Please enter a valid latitude.')
        return value

    def clean_longitude(self):
        value = self.cleaned_data.get('longitude')
        if not value:
            return value
        try:
            value = float(value)
        except (ValueError, TypeError):
            raise ValidationError('Please enter a valid longitude.')
        return value


    class Meta:
        model = Sighting
        fields = ['animal',
                  'count',
                  'observed_at_date',
                  'observed_at_time',
                  'latitude',
                  'longitude',
                  'notes',
                  'animal_image',
                  ]

        help_texts = {
            'animal': 'Animal',
            'observed_at_date': 'Observed at - date',
            'observed_at_time': 'Observed at - time',
            'count': 'Count',
            'latitude': 'Latitude',
            'longitude': 'Longitude',
            'notes': 'Notes',
            'animal_image': 'Animal Image',
        }

        error_messages = {
            'animal': {
                'required': 'Animal is a required field.',
            },
            'count': {
                'required': 'Animal count is a required field.',
                'invalid': 'Please enter a valid count.',
            },
            'observed_at_date': {
                'required': 'Observed at - date is a required field.',
            },
            'observed_at_time': {
                'required': 'Observed at - date is a required field.',
            },
            'notes': {
                'max_length': 'Cannot exceed 500 characters.',
            },
        }


        widgets = {
            'animal': forms.Select(attrs={
                'class': 'border rounded-sm p-2 w-full bg-white',
                'placeholder': 'Choose an animal',
            }),
            'observed_at_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'border rounded-sm p-2 w-full bg-white',
            }),
            'observed_at_time': forms.TimeInput(attrs={
                'type': 'time',
                'class': 'border rounded-sm p-2 w-full bg-white',
                'placeholder': 'Click to select time.',
                'id': 'timepicker',
            }),
            'count': forms.TextInput(attrs={
                'class': 'border rounded-sm p-2 w-full bg-white'
            }),
            'latitude': forms.TextInput(attrs={
                'class': 'border rounded-sm p-2 w-full bg-white appearance-none',
                'placeholder': '-90 to 90',
            }),
            'longitude': forms.TextInput(attrs={
                'class': 'border rounded-sm p-2 w-full bg-white',
                'placeholder': '-180 to 180',
            }),
            'notes': forms.Textarea(attrs={
                'style': 'resize:none;',
                'rows': '4',
                'class': 'border rounded-sm p-2 w-full bg-white',
            }),
            "animal_image": forms.FileInput(attrs={
                'class': 'block w-full text-sm text-gray-500 '
                         'file:mr-4 file:py-2 file:px-4 file:rounded-sm file:border-0 '
                         'file:bg-gray-500 file:text-white hover:file:bg-gray-600 bg-white',
                'id': 'id_animal_image',
            }),
        }


class SightingDeletingForm(SightingForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.read_only = True
            field.disabled = True

