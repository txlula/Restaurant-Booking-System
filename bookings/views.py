from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from bookings.models import LoginStaffAccountForm, RegisterStaffAccountForm, \
    RegisterStaffForm, Account, Person, Reservation
import datetime

#Start Page
def start(request):
    return render(request, 'bookings/start.html',)

#Staff Login Page
def staffloginscreen(request):
    if request.method == "post":
        form = LoginStaffAccountForm(request.POST)
        if form.is_valid():
            user = Account(username = 'username', password = 'password')
            user.save()
    else:
        form = LoginStaffAccountForm()
    return render(request, 'bookings/stafflogin.html', context={"form":form})

#Staff Register Page
def staffregister(request):
    if request.method == "post":
        form = RegisterStaffAccountForm(request.POST)
        if form.is_valid():
            newuser = Account(username = 'username', password = 'password', 
                                   first_name = 'first_name', second_name = 'second_name',
                                   email = 'email')
            newuser.save()
    else:
        form = RegisterStaffAccountForm()
    return render(request, 'bookings/staffregister.html', context={"form":form})

#Staff Home
def staffhome(request):
    return render(request, 'bookings/staffhome.html',)