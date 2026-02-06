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
                'class': 'border rounded-sm m-2 p-2 w-full',
                'placeholder': 'Enter expedition title',
            }),
            'primary_animal': forms.Select(attrs={
                'class': 'border rounded-sm m-2 p-2 w-full appearance-none',
                'style': 'background-color: white;',
                'placeholder': 'Choose an animal',
            }),
            'additional_animals': forms.CheckboxSelectMultiple(attrs={
            }),
            'description': forms.Textarea(attrs={
                'style':'resize:none;',
                'rows':'5',
                'class': 'border rounded-sm m-2 p-2 w-full',

            }),
            'location': forms.TextInput(attrs={
                'class': 'border rounded-sm m-2 p-2 w-full',
                'placeholder': 'e.g, Amazon Rainforest, Brazil'
            }),
            "animal_image": forms.FileInput(attrs={
                'class': 'hidden border rounded-sm m-2 p-2 w-full appearance-none',
                'style': 'background-color: white;'
            }),
        }



