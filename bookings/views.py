from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from bookings.models import *

from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.core.mail import send_mail

#Start Page
def start(request):
    context = {}
    restaurants = Restaurant.objects.all()

    form = SearchRestaurantForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data.get('restaurant_name')
        restaurants = Restaurant.objects.filter(rest_name = name)
        context.update({'restaurants' : restaurants, 'form' : form})
    else:
        form = SearchRestaurantForm()

    context.update({'restaurants' : restaurants, 'form' : form})
    return render(request, 'bookings/start.html', context)

#Staff Login Page
def stafflogin(request):
    next = request.GET.get('next')
    form = LoginForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username = username, password = password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/staffhome')
    return render(request, 'bookings/stafflogin.html', {'form' : form})

#Staff Register Page
def staffregister(request):
    next = request.GET.get('next')
    form = RegisterForm(request.POST)
    if form.is_valid():
        #Save form data but database is not updated
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new = authenticate(username = user.username, password = password)
        login(request,user)
        if next:
            return redirect(next)
        return redirect('/staffhome')
    return render(request, 'bookings/staffregister.html', {'form' : form})

#Staff Logout Page
def stafflogout(request):
    logout(request)
    return redirect('/')

@login_required
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
    notification_list = Notifications()
    for reservation in reservations:
        notification_list.enqueue(reservation)

    context.update({'reservations' : reservations})
        
    return render(request, 'bookings/staffhome.html', context)

#Remove reservation function
def remove_reservation(request, reservation_id=None):
        r = Reservation.objects.get(reservationID = reservation_id).delete()
        return HttpResponseRedirect("/staffhome")

#Reserve Page
def reserve(request, restaurant_id=None):
    context = {}
    reserveform = ReserveForm(request.POST)
    personform = CustomerForm(request.POST)

    if reserveform.is_valid():
        reservation = reserveform.save(commit=False)
        r_id = reserveform.cleaned_data.get('reservationID')
        reservation.save()

        restaurantID = Restaurant.objects.get(restaurantID = restaurant_id)
        reservation.restaurant_id = restaurantID
        reservation.save(update_fields=['restaurant_id'])

        if personform.is_valid():
            customer = personform.save()
            customer.reservation_id = r_id
            customer.save(update_fields=['reservation_id'])

            messages.success(request, 'You have reserved a table.')
    else:
        reserveform = ReserveForm()
        personform = CustomerForm()
    
    #Confirmation of reservation sent by email
    '''
    send_mail("Reservation Confirmation", "Dear {} {}, \
    Thank you for reserving a table for at {}. \
    Reservation information: \
    Number of people dining: {} \
    Date of reservation: {} \
    Time of reservation: {} \
    Additional information: {} \
    Restaurant information: \
    Restaurant address: {} \
    Restaurant phone number: {}", )
    '''

    context.update({'reserveform' : reserveform, 'personform': personform})
    return render(request, 'bookings/reserve.html', context)

#Menu Page
def menu(request):
    context = {}
    dishes = Dish.objects.all()

    AddDish = AddDishForm(request.POST)
    if AddDish.is_valid():
        dish = AddDish.save()
    else:
        AddDish = AddDishForm()

    context.update({'form' : AddDish, 'dishes' : dishes})
    return render(request, 'bookings/menu.html', context)

#Remove dish function
def remove_dish(request, dish_id=None):
        d = Dish.objects.get(dishID = dish_id).delete()
        return HttpResponseRedirect("/menu")