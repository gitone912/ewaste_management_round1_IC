from django.urls import path
from . import views

urlpatterns = [
#    user authentication
    path("register/", views.Register, name="register"),
    path("login/", views.Login, name="login"),
    path("logout/", views.Logout, name="logout"),
    path("map/", views.map, name="map"),
    path("", views.home , name='home'),
    # path("bins/", views.bins, name="bins"),
    # path("mapping/", views.mapping, name="mapping"),
    path("new_bin/", views.new_bins, name="new_bins"),
    path("new_mapping/", views.new_mapping, name="new_mapping"),
    path("camera_vision/", views.camera_v, name="camera_vision"),
    path('cvmap/', views.cvmap, name='cvmap'),
]