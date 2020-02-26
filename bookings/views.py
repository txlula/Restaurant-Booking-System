from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from bookings.models import *

from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


#Start Page
def start(request):
    context = {}
    restaurants = Restaurant.objects.all()

    #Searching restaurant form
    form = SearchRestaurantForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data.get('restaurant_name')
        #If the name the user has inputted is in the database, the restaurant information will be displayed
        restaurants = Restaurant.objects.filter(rest_name = name)
        context.update({'restaurants' : restaurants, 'form' : form})
    else:
        form = SearchRestaurantForm()

    context.update({'restaurants' : restaurants, 'form' : form})
    return render(request, 'bookings/start.html', context)

#Staff Login Page
def stafflogin(request):
    #Login form
    form = LoginForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        #If the username and password inputted is in the database, the user can login
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('/staffhome')
    return render(request, 'bookings/stafflogin.html', {'form' : form})

#Staff Register Page
def staffregister(request):
    context = {}
    #Register form that saves to Staff and Restaurant model
    registerform = RegisterForm(request.POST)
    restinfoform = RestaurantInfoForm(request.POST)

    if registerform.is_valid() and restinfoform.is_valid():
        #Save form data but database is not updated
        info = restinfoform.save(commit=False)
        id = restinfoform.cleaned_data.get('restaurantID')
        info.save()

        #Save form data but database is not updated
        user = registerform.save(commit=False)
        #Check if username is unique
        username = registerform.cleaned_data.get('username')
        e = User.objects.filter(username = username)
        if e == username:
            messages.error(request, 'This username is not available. Try a different one.')
        else:
            password = registerform.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            #The user wil automatically be redirected to the staff home page
            new = authenticate(username = user.username, password = password)
            login(request,user)
            return redirect('/staffhome')
    else:
        registerform = RegisterForm()
        restinforform = RestaurantInfoForm()

    context.update({'registerform' : registerform, 'restinfoform' : restinfoform})
    return render(request, 'bookings/staffregister.html', context)

#Staff Logout Page
def stafflogout(request):
    logout(request)
    #Redirects user to start page
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

    #List of reservations is ordered by date of booking
    reservations = Reservation.objects.all().order_by('date_of_booking')
    notification_list = Notifications()
    #Reservation is added to queue
    for reservation in reservations:
        notification_list.enqueue(reservation)

    context.update({'reservations' : reservations})
        
    return render(request, 'bookings/staffhome.html', context)

@login_required
#Remove reservation function
def remove_reservation(request, reservation_id=None):
        #The reservation id is searched in the database
        #The reservation is deleted from the database
        r = Reservation.objects.get(reservationID = reservation_id).delete()
        return HttpResponseRedirect("/staffhome")

#Reserve Page
def reserve(request, restaurant_id=None):
    context = {}
    #Form to save information to Customer and Reservation model
    reserveform = ReserveForm(request.POST)
    personform = CustomerForm(request.POST)

    if reserveform.is_valid() and personform.is_valid():
        reservation = reserveform.save(commit=False)
        customer = personform.save()

        #The reservation id is saved to the customer model
        r_id = reserveform.cleaned_data.get('reservationID')
        customer.reservation_id = r_id
        customer.save(update_fields=['reservation_id'])

        #Validation to check if number of people inputted is 0
        people = reserveform.cleaned_data.get('no_of_people')
        if people <= 0:
            messages.error(request, 'Number cannot be 0')
        else:
            reservation.save()

            #The restaurant id is saved to the reservation model
            restaurantID = Restaurant.objects.get(restaurantID = restaurant_id)
            reservation.restaurant_id = restaurantID
            reservation.save(update_fields=['restaurant_id'])

            #The customer has successfully reserved a table if the validation test passes
            messages.success(request, 'You have reserved a table.')
    else:
        reserveform = ReserveForm()
        personform = CustomerForm()

    context.update({'reserveform' : reserveform, 'personform': personform})
    return render(request, 'bookings/reserve.html', context)

@login_required
#Menu Page
def menu(request, restaurant_id=None):
    context = {}
    #Shows list of dishes
    dishes = Dish.objects.all()

    #Form to add dish
    AddDish = AddDishForm(request.POST)
    if AddDish.is_valid():
        dish = AddDish.save()
    else:
        AddDish = AddDishForm()

    #Form to add menu
    AddMenu = AddMenuFile(request.POST, request.FILES)

    context.update({'AddDish' : AddDish, 'AddMenu' : AddMenu, 'dishes' : dishes})
    return render(request, 'bookings/menu.html', context)

@login_required
#Remove dish function
def remove_dish(request, dish_id):
        d = Dish.objects.get(dishID = dish_id).delete()
        return HttpResponseRedirect("/menu")

@login_required
#Restaurant Information Page
def restaurant_info(request):
    context = {}
    form = RestaurantInfoForm(request.POST)
    context.update({'form' : form})
    return render(request, 'bookings/restaurantinfo.html', context)