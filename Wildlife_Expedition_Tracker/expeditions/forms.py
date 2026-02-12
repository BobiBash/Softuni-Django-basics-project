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
                'class': 'border rounded-sm p-2 w-full',
                'style': 'background-color: white;',
                'placeholder': 'Enter expedition title',
            }),
            'target_species': forms.Select(attrs={
                'class': 'border rounded-sm p-2 w-full appearance-none',
                'style': 'background-color: white;',
                'placeholder': 'Choose an animal',
            }),
            'expected_species': forms.CheckboxSelectMultiple(attrs={
                'class': 'flex-inline'
            }),
            'description': forms.Textarea(attrs={
                'style':'resize:none; background-color: white',
                'rows':'5',
                'class': 'border rounded-sm p-2 w-full',

            }),
            'location': forms.TextInput(attrs={
                'class': 'border rounded-sm p-2 w-full',
                'style': 'background-color: white;',
                'placeholder': 'e.g, Amazon Rainforest, Brazil'
            }),
            # "animal_image": forms.FileInput(attrs={
            #     'class': 'block w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-sm file:border-0 file:bg-gray-500 file:text-white hover:file:bg-gray-600',
            #     'style': 'background-color: white;',
            #     'id': 'id_animal_image',
            # }),
        }

class ExpeditionDeleteForm(ExpeditionForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.disabled = True
            field.read_only = True
