from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from bookings.models import *
import datetime

#Start Page
def start(request):
    restaurants = Restaurant.objects.all()
    context = {'restaurants' : restaurants}
    return render(request, 'bookings/start.html', context)

#Staff Login Page
def staffloginscreen(request):
    loginform = LoginStaffAccountForm(request.POST)
    return render(request, 'bookings/stafflogin.html', {'form' : loginform})

#Staff Register Page
def staffregister(request):
    registerform = RegisterStaffAccountForm(request.POST)
    return render(request, 'bookings/staffregister.html', {'form' : registerform})

#Staff Home
def staffhome(request):
    return render(request, 'bookings/staffhome.html',)

#Reserve Page
def reserve(request):
    reserveform = ReserveForm(request.POST)
    if reserveform.is_valid():
        Reservation = reserveform.save()
    return render(request, 'bookings/reserve.html', {'form' : reserveform})