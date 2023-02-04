from django.db import models
from django import forms
from django.contrib.auth.models import User
# Create your models here.

selection = (
    ('y', 'filled'),
    ('n', 'notfilled'),
    )
class bin_status(models.Model):
    location_name = models.CharField(max_length=200, null=True,blank=True)
    lat = models.DecimalField(blank=True, null=True, max_digits=20,  decimal_places=10 , unique=True)
    lng = models.DecimalField(blank=True, null=True, max_digits=20,  decimal_places=10 , unique=True)
    status = models.CharField(max_length=60, blank=True, default='',choices=selection,verbose_name="status")
    image= models.ImageField(upload_to="profile_pics", blank=True, null=True )
    def __str__(self):
        return (f"{self.location_name}:({self.lat}-{self.lng})")
    
class camera_vision(models.Model):
    #location1
    location_name = models.CharField(max_length=200, null=True,blank=True)
    loc_lat = models.DecimalField(blank=True, null=True, max_digits=20,  decimal_places=10 , unique=True)
    loc_lng = models.DecimalField(blank=True, null=True, max_digits=20,  decimal_places=10 , unique=True)
    locimage = models.ImageField(upload_to="profile_pics", blank=True, null=True)
    def __str__(self):
        return (f"{self.location_name}:({self.loc_lat}-{self.loc_lng})")
    
check=(
    ('y', 'yes'),
    ('n', 'no')
)
class arduino(models.Model):
    check_filled = models.ForeignKey(bin_status, on_delete=models.CASCADE, blank=True, null=True,verbose_name="check_filled",unique=True)
    distance = models.IntegerField(blank=True, null=True, default=0,verbose_name="distance")
    fill_img = models.IntegerField(blank=True, null=True, default=0,verbose_name="fill_img")
    
position = (
    ('admin','admin'),
    ('driver','driver'),
    )
class u_details(models.Model):
    user_name = models.ForeignKey(User,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200, null=True,blank=True)
    status = models.CharField(max_length=60, blank=True, default='',choices=position,verbose_name="status")
    address = models.CharField(max_length=200, null=True,blank=True)
    area_assigned = models.CharField(max_length=200, null=True,blank=True)
    email=models.EmailField(max_length=200, null=True,blank=True)
    def __str__(self):
        return (f"{self.full_name}")
    