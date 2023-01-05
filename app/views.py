import json
from django.shortcuts import render
from django.contrib.auth  import authenticate,  login, logout 
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
import numpy as np
from .models import *
from .forms import *
from .prediction import cpy

# Create your views here.
def home(request):
    return render(request, 'body.html')

def Register(request):
    if request.method != "POST":
        return render(request, "register.html")
    username = request.POST['username']
    email = request.POST['email']
    first_name=request.POST['first_name']
    last_name=request.POST['last_name']
    password1 = request.POST['password1']
    password2 = request.POST['password2']

    if password1 != password2:
        messages.error(request, "Passwords do not match.")
        return redirect('/register')

    user = User.objects.create_user(username, email, password1)
    user.first_name = first_name
    user.last_name = last_name
    user.save()
    return render(request, 'login.html')

def Login(request):
    if request.method != "POST":
        return render(request, "login.html")
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        messages.success(request, "Successfully Logged In")
        return render(request ,'after_login.html')
    else:
        messages.error(request, "Invalid Credentials")
    return render(request ,'after_login.html')


def Logout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/login')


def map(request):  # sourcery skip: dict-comprehension, for-index-replacement, move-assign-in-block, remove-zero-from-range
    lat_values = {}
    lng_values = {}
    l1=camera_vision.objects.all().values()
    print(l1)
    locations = bin_status.objects.filter(status="y").values()
    values=list(locations)
    for i in range(len(values)):
        lat_values[i] = values[i]['lat']
        lng_values[i]=values[i]['lng']
    resultList1 = list(lat_values.values())
    resultList2 = list(lng_values.values())
    for i in range(len(resultList1)):
        resultList1[i] = float(resultList1[i])
        resultList2[i] = float(resultList2[i])
    overall = np.array(list(zip(resultList1, resultList2)))
    data = json.dumps(overall.tolist())
    return render(request, 'map.html', {'data': data})


def new_bins(request):
    data = bin_status.objects.all()
    if request.method == "POST":
        fm = map_status(request.POST)
        
        if fm.is_valid():
            reg = bin_status(lat=fm.cleaned_data['lat'],lng=fm.cleaned_data['lng'],status=fm.cleaned_data['status'])
            reg.save()
            #return HttpResponseRedirect("/new_bin/")
            return render(request ,'new_bins.html',{'form': fm,'data':data})
    else:
        fm = map_status()
    return render(request ,'new_bins.html',{'form': fm,'data':data})
    
def new_mapping(request):
    return render(request, 'new_mapping.html')

def camera_v(request):  # sourcery skip: extract-method
    data = camera_vision.objects.all()
    if request.method == "POST":
        fm = camera(request.POST , request.FILES)
        if fm.is_valid():
            locimage = cpy.get_image(fm.cleaned_data['locimage'])
            if locimage == 1:
                reg=camera_vision(loc_lat=fm.cleaned_data['loc_lat'],loc_lng=fm.cleaned_data['loc_lng'],locimage=fm.cleaned_data['locimage'])
                reg.save()
            #return HttpResponseRedirect("/camera_vision/")
            return render(request, "camera_v.html", {'form':fm,'data':data})
    else:
        fm = camera()
    return render(request, "camera_v.html", {'form':fm,'data':data})

def cvmap(request):  # sourcery skip: dict-comprehension, for-index-replacement, move-assign-in-block, remove-zero-from-range
    lat_values = {}
    lng_values = {}
    locations = camera_vision.objects.all().values()
    values=list(locations)
    for i in range(len(values)):
        lat_values[i] = values[i]['loc_lat']
        lng_values[i]=values[i]['loc_lng']
    resultList1 = list(lat_values.values())
    resultList2 = list(lng_values.values())
    for i in range(len(resultList1)):
        resultList1[i] = float(resultList1[i])
        resultList2[i] = float(resultList2[i])
    overall = np.array(list(zip(resultList1, resultList2)))
    data = json.dumps(overall.tolist())
    return render(request, 'map.html', {'data': data})

def update_data(request,pk):#bin
    order = bin_status.objects.get(id=pk)
    form = map_status(instance=order)
    if request.method == "POST":
        fm = map_status(request.POST,instance=order)
        if fm.is_valid():
            fm.save()
            return redirect("new_bins")
            #return render(request ,'new_bins.html',{'form': fm,'data':data})
    return render(request, 'update.html', {'form': form})
    
def delete_data(request,pk):#bin
    order = bin_status.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect("new_bins")
    return render(request, 'delete.html', {'data': order})

#cv
def update_cvdata(request,pk):
    order = camera_vision.objects.get(id=pk)
    form = camera(instance=order)
    if request.method == "POST":
        fm = camera(request.POST,instance=order)
        if fm.is_valid():
            fm.save()
            return redirect("camera_vision")
            #return render(request ,'new_bins.html',{'form': fm,'data':data})
    return render(request, 'update.html', {'form': form})
    
def delete_cvdata(request,pk):
    order = camera_vision.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect("camera_vision")
    return render(request, 'deletecv.html', {'data': order})