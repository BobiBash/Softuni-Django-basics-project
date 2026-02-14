from django import forms

from .models import Expedition


class ExpeditionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['target_species'].empty_label = 'Choose an animal'

    class Meta:
        model = Expedition
        fields = ['title',
                  'target_species',
                  'expected_species',
                  'description',
                  'location',
                  ]

        help_texts = {
            "title": "Title",
            'target_species': 'Target Species',
            'expected_species': 'Expected Species',
            'description': 'Description',
            'location': 'Location',
        }


        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'border rounded-sm p-2 w-full bg-white',
                'placeholder': 'Enter expedition title',
            }),
            'target_species': forms.Select(attrs={
                'class': 'border rounded-sm p-2 w-full bg-white',
                'placeholder': 'Choose an animal',
            }),
            'expected_species': forms.CheckboxSelectMultiple(attrs={
                'class': 'flex-inline'
            }),
            'description': forms.Textarea(attrs={
                'style':'resize:none;',
                'rows':'5',
                'class': 'border rounded-sm p-2 w-full bg-white',

            }),
            'location': forms.TextInput(attrs={
                'class': 'border rounded-sm p-2 w-full bg-white',
                'placeholder': 'e.g, Amazon Rainforest, Brazil'
            }),
        }

class ExpeditionDeleteForm(ExpeditionForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.disabled = True
            field.read_only = True
