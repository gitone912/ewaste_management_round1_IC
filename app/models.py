from django.db import models
from django import forms
# Create your models here.

selection = (
    ('y', 'filled'),
    ('n', 'notfilled'),
    )
class bin_status(models.Model):
    lat = models.DecimalField(blank=True, null=True, max_digits=20,  decimal_places=10)
    lng = models.DecimalField(blank=True, null=True, max_digits=20,  decimal_places=10)
    status = models.CharField(max_length=60, blank=True, default='',choices=selection,verbose_name="status")
    
class camera_vision(models.Model):
    #location1
    loc_lat = models.DecimalField(blank=True, null=True, max_digits=20,  decimal_places=10)
    loc_lng = models.DecimalField(blank=True, null=True, max_digits=20,  decimal_places=10)
    locimage = models.ImageField(upload_to="profile_pics", blank=True, null=True)
    