from django import forms

from .validators import validate_time
from .models import Sighting

class SightingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['animal'].empty_label = 'Choose an animal'


    observed_at_time = forms.TimeField(
        help_text='Observed at - time',
        input_formats=['%H:%M', '%I:%M %p', '%H:%M:%S'],
        validators=[validate_time],
        error_messages={
            'invalid': 'Invalid time. Use HH:MM format',
            'required': 'Required field',
        },
        widget=forms.TimeInput(attrs={
            'type': 'text',
            'class': 'border rounded-sm p-2 w-full bg-white',
            'placeholder': 'HH:MM (e.g., 14:30)',
            'pattern': '[0-2][0-9]:[0-5][0-9]:[0-5][0-9]',
        }),
    )


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
            'latitude': 'Latitude(-90 to 90)',
            'longitude': 'Longitude(-180 to 180)',
            'notes': 'Notes',
            'animal_image': 'Animal Image',
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
            'count': forms.NumberInput(attrs={
                'class': 'border rounded-sm p-2 w-full bg-white'
            }),
            'latitude': forms.NumberInput(attrs={
                'class': 'border rounded-sm p-2 w-full bg-white appearance-none',
            }),
            'longitude': forms.NumberInput(attrs={
                'class': 'border rounded-sm p-2 w-full bg-white',
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

