from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.list import ListView

from bookings.models import *

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages

#Start Page
def start(request):
    restaurants = Restaurant.objects.raw('SELECT * FROM bookings_Restaurant')
    context = {'restaurants' : restaurants}
    return render(request, 'bookings/start.html', context)

#Staff Login Page
def staffloginscreen(request):
    if request.method == 'post':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('staffhome')
    else:
        form = AuthenticationForm()
    return render(request, 'bookings/stafflogin.html', {'form' : form})

#Staff Register Page
def staffregister(request):
    if request.method == 'post':
        form = RegisterStaffForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            messages.success(request, 'Account has been created.')
            return redirect('staffhome')
    else:
        form = RegisterStaffForm()
    return render(request, 'bookings/staffregister.html', {'form' : form})

#Staff Home
def staffhome(request):
    context = {}

    #Implementing notifications using a circular queue
    class Notifications:
        #Implement queue
        def __init__(self):
            self.queue = list()
            self.front = 0
            self.rear = 0
            self.maxSize = 6
            self.size = len(self.queue)
            QueueFull = False

        #Adding items to queue
        def enqueue(self, item):
            if self.size == self.maxSize - 1:
                QueueFull = True
            self.queue.append(item)
            self.rear = (self.rear + 1) % self.maxSize

        #Removing items from queue
        def dequeue(self):
            if self.size == 0:
                QueueEmpty = True
            item = self.queue[self.front]
            self.front = (self.front + 1) % self.maxSize
            return item

    reservations = Reservation.objects.all()
    context.update({'reservations' : reservations})
        
    return render(request, 'bookings/staffhome.html', context)

#Reserve Page
def reserve(request):
    context = {}
    reserveform = ReserveForm(request.POST)
    personform = CustomerForm(request.POST)

    if reserveform.is_valid() and personform.is_valid():
        Reservation = reserveform.save()
        Person = personform.save()
        messages.success(request, 'You have reserved a table.')
    else:
        reserveform = ReserveForm()
        personform = CustomerForm()
    
    messages.info(request, 'Time should be in 24:00 format')
    context.update({'reserveform' : reserveform, 'personform': personform})
    return render(request, 'bookings/reserve.html', context)

#Menu Page
def menu(request):
    dishes = Dish.objects.raw('SELECT * FROM bookings_Dish')
    context = {'dishes' : dishes}

    AddDish = AddDishForm(request.POST)

    if AddDish.is_valid():
        Dish = AddDish.save()
    else:
        AddDish = AddDishForm()
    return render(request, 'bookings/menu.html', context, {'form' : AddDish})