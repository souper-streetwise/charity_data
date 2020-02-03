from django import forms
from django.forms import ModelForm
from .models import Record

# create the form class for the Record model
class RecordForm(ModelForm):
	class Meta:
		model = Record
		fields = '__all__'
#		fields = ['charity', 'time', 'location']