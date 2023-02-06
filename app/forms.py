from django import forms
from django.forms import TextInput
from .models import *
from fractions import Fraction

class map_status(forms.ModelForm):
    def __init__(self, *args, **kargs):
        super(map_status, self).__init__(*args, **kargs)
    class Meta:
        model = bin_status
        fields = ['location_name','lng','lat','image','status']
        widgets = {
            'location_name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Enter the location name'
                }),
             'lng': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Enter Latitude'
                }),
            'lat': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Enter Longitude'
                }),
           
        }
        
class camera(forms.ModelForm):
    def __init__(self, *args, **kargs):
        super(camera, self).__init__(*args, **kargs)
    class Meta:
        model = camera_vision
        fields = ['location_name','loc_lng','loc_lat','locimage']
        widgets = {
            'location_name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Enter the location name'
                }),
            'loc_lng': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Enter Latitude'
                }),
            'loc_lat': TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Enter Longitude'
                })
        }

class arduino_status(forms.ModelForm):
    def __init__(self, *args, **kargs):
        super(arduino_status, self).__init__(*args, **kargs)
    class Meta:
        model = arduino
        fields = ['check_filled']
        