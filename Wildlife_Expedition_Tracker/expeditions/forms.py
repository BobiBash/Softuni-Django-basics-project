from django import forms

from .models import Expedition


class ExpeditionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['primary_animal'].empty_label = 'Choose an animal'

    class Meta:
        model = Expedition
        fields = ['title',
                  'primary_animal',
                  'additional_animals',
                  'description',
                  'location',
                  'animal_image']



        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'border rounded-sm p-2 w-full',
                'style': 'background-color: white;',
                'placeholder': 'Enter expedition title',
            }),
            'primary_animal': forms.Select(attrs={
                'class': 'border rounded-sm p-2 w-full appearance-none',
                'style': 'background-color: white;',
                'placeholder': 'Choose an animal',
            }),
            'additional_animals': forms.CheckboxSelectMultiple(attrs={
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
            "animal_image": forms.FileInput(attrs={
                'class': 'block w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-sm file:border-0 file:bg-gray-500 file:text-white hover:file:bg-gray-600',
                'style': 'background-color: white;',
                'id': 'id_animal_image',
            }),
        }



