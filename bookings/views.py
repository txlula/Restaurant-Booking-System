from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

#Import all models
from bookings.models import *

from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages

#Start Page
def start(request):
    '''
    restaurants = Restaurant.objects.all()
    context = {'restaurants' : restaurants}
    '''
    restaurants = Restaurant.objects.raw('SELECT * FROM Restaurant')
    context = {'restaurants' : restaurants}

    if request.method == 'post':
        form = SearchRestaurant(request.POST)
    else:
        form = SearchRestaurant()
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
    reservations = Reservation.objects.all()
    context = {'reservations' : reservations}

    #Implementing notifications using a circular queue
    class NotificationsQueue:
        def __init__(self):
            self.queue = list()
            self.front = 0
            self.rear = 0
            self.maxSize = 6
        
    return render(request, 'bookings/staffhome.html', context)

#Reserve Page
def reserve(request):
    reserveform = ReserveForm(request.POST)
    #Validation
    if reserveform.is_valid():
        Reservation = reserveform.save()
        messages.success(request, 'You have reserved a table.')
    else:
        #messages.error(request, 'Choose a different time.')
        reserveform = ReserveForm()

    return render(request, 'bookings/reserve.html', {'form' : reserveform})