from django import forms
from django.forms import TextInput
from .models import *


class map_status(forms.ModelForm):
    def __init__(self, *args, **kargs):
        super(map_status, self).__init__(*args, **kargs)
    class Meta:
        model = bin_status
        fields = ['lng','lat','status']
        widgets = {
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
        fields = ['loc_lng','loc_lat','locimage']
        widgets = {
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
        