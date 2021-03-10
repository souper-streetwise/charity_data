from django import forms
from django.forms import ModelForm
from .models import Record


# create the form class for the Record model
class RecordForm(ModelForm):
    # item = forms.ModelChoiceField(
    #     queryset=Item.objects.all(),
    #     empty_label="Please select an item..."
    # )

    class Meta:
        model = Record
        fields = ['quantity', 'location']
        widgets = {
            'location': forms.TextInput(
                attrs={
                    'readonly': 'true',
                    'placeholder': 'Retrieving...'
                },
            ),
        }
