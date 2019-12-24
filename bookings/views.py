from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from bookings.models import *
import datetime
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

#Start Page
def start(request):
    restaurants = Restaurant.objects.all()
    context = {'restaurants' : restaurants}
    return render(request, 'bookings/start.html', context)

#Staff Login Page
def staffloginscreen(request):
    form = AuthenticationForm()

    if request.method == 'post':
        form = AuthenticationForm(data=request.POST)

        #Validation
        if form.is_valid():
            user = form.get_user()
    else:
        form = AuthenticationForm()
    return render(request, 'bookings/stafflogin.html', {'form' : form})

#Staff Register Page
def staffregister(request):
    form = UserCreationForm()
    registerpersonform = RegisterStaffForm()

    if request.method == 'post':
        form = UserCreationForm(request.POST)
        registerpersonform = RegisterStaffForm(request.POST)

        #Validation
        if form.is_valid() and registerpersonform.is_valid():
            user = form.save()
            Person = registerpersonform.save()
    else:
        form = UserCreationForm()
        registerpersonform = RegisterStaffForm()
    return render(request, 'bookings/staffregister.html', {'form' : form,
                                                          'registerpersonform' : registerpersonform})

#Staff Home
def staffhome(request):
    return render(request, 'bookings/staffhome.html',)

#Reserve Page
def reserve(request):
    reserveform = ReserveForm(request.POST)
    #Validation
    if reserveform.is_valid():
        Reservation = reserveform.save()
    else:
        reserveform = ReserveForm()

    return render(request, 'bookings/reserve.html', {'form' : reserveform})