from django import forms
from .models import Resource
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['resource', 'user_name', 'date', 'start_time', 'end_time']

class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['name', 'description']
