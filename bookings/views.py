from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from bookings.models import *
import datetime

'''
import sqlite3
conn = sqlite3.connect('db.sqlite3')
'''

#Start Page
def start(request):
    restaurants = Restaurant.objects.all()
    context = {'restaurants' : restaurants}
    return render(request, 'bookings/start.html', context)

#Staff Login Page
def staffloginscreen(request):
    if request.method == "post":
        if request.post.get('username') and request.post.get('password'):
            account = Account()
            account.username = request.post.get('username')
            account.password = request.post.get('password')
            account.save()
            return render(request, 'bookings/stafflogin.html',)
    else:
        return render(request, 'bookings/stafflogin.html',)

#Staff Register Page
def staffregister(request):
    if request.method == "post":
        if request.post.get('first_name') and request.post.get('second_name') and request.post.get('email')\
        and request.post.get('username') and request.post.get('password'):
            person = Person()
            person.first_name = request.post.get('first_name')
            person.second_name = request.post.get('second_name')
            person.email = request.post.get('email')
            person.username = request.post.get('username')
            person.password = request.post.get('password')
            newuser.save()
            return render(request, 'bookings/staffregister.html',)
    else:
        return render(request, 'bookings/staffregister.html',)

#Staff Home
def staffhome(request):
    return render(request, 'bookings/staffhome.html',)

#Reserve Page
def reserve(request):
    form = ReserveForm()
    if request.method == "post":
        if form.is_valid():
            form.save()
        else:
            form = ReserveForm()
    return render(request, 'bookings/reserve.html', {'form' : form})