from django.db import models
from django import forms
# Create your models here.

selection = (
    ('y', 'filled'),
    ('n', 'notfilled'),
    )
class bin_status(models.Model):
    lat = models.DecimalField(blank=True, null=True, max_digits=20,  decimal_places=10 , unique=True)
    lng = models.DecimalField(blank=True, null=True, max_digits=20,  decimal_places=10 , unique=True)
    status = models.CharField(max_length=60, blank=True, default='',choices=selection,verbose_name="status" )
    def __str__(self):
        return (f"{self.lat}-{self.lng}")
    
class camera_vision(models.Model):
    #location1
    loc_lat = models.DecimalField(blank=True, null=True, max_digits=20,  decimal_places=10 , unique=True)
    loc_lng = models.DecimalField(blank=True, null=True, max_digits=20,  decimal_places=10 , unique=True)
    locimage = models.ImageField(upload_to="profile_pics", blank=True, null=True )
    
check=(
    ('y', 'yes'),
    ('n', 'no')
)
class arduino(models.Model):
    check_filled = models.ForeignKey(bin_status, on_delete=models.CASCADE, blank=True, null=True,verbose_name="check_filled")
    distance = models.IntegerField(blank=True, null=True, default=0,verbose_name="distance")
    fill_img = models.IntegerField(blank=True, null=True, default=0,verbose_name="fill_img")