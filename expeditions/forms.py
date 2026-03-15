from django import forms

from .models import Expedition


class ExpeditionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['target_species'].empty_label = 'Choose an animal'


    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')
        if not start_date < end_date:
            raise forms.ValidationError("End date must be after start date.")
        return cleaned_data

    class Meta:
        model = Expedition
        fields = ['title',
                  'target_species',
                  'expected_species',
                  'description',
                  'location',
                  'start_date',
                  'end_date',
                  ]

        help_texts = {
            "title": "Title",
            'target_species': 'Target Species',
            'expected_species': 'Expected Species',
            'description': 'Description',
            'location': 'Location',
            'start_date': 'Start Date',
            'end_date': "End Date",
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
            'start_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'border rounded-sm p-2 w-full bg-white',
            }),
            'end_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'border rounded-sm p-2 w-full bg-white',
            }),
        }

class ExpeditionDeleteForm(ExpeditionForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.disabled = True
            field.read_only = True
