from django.db import models
from django.forms import ModelForm
from django import forms

#Restaurant Model
class Restaurant(models.Model):
    restaurantID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300)
    address = models.TextField()
    phone_no = models.PositiveIntegerField()
    max_size = models.PositiveIntegerField()

#Person Model
class Person(models.Model):
    personID = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    phone_no = models.PositiveIntegerField()
    email = models.EmailField(max_length=300)

#Account Model
class Account(models.Model):
    accountID = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    Person = models.ForeignKey(Person, on_delete=models.CASCADE)
    Restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

#Reservation Model
class Reservation(models.Model):
    reservationID = models.AutoField(primary_key=True)
    no_of_people = models.PositiveIntegerField()
    date_of_booking = models.DateField()
    time_of_booking = models.TimeField(unique=True)
    Person = models.ForeignKey(Person, on_delete=models.CASCADE)

#Dish Model
class Dish(models.Model):
	dishID = models.AutoField(primary_key=True)
	name = models.CharField(max_length=200)
	price = models.DecimalField(max_digits=5, decimal_places=2)

#Order Model
class Order(models.Model):
    orderID = models.AutoField(primary_key=True)
    time = models.DateTimeField()
    address = models.TextField()
    Dish = models.ForeignKey(Dish, on_delete=models.CASCADE)

#Form to reserve with Reservation Model
class ReserveForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ['no_of_people', 'date_of_booking', 'time_of_booking']

#Form for customer's input when reserving
class CustomerForm(ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'second_name', 'phone_no', 'email']

#Form to register staff with Account Model
class RegisterStaffAccountForm(ModelForm):
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)
    class Meta:
        model = Account
        fields = ['username', 'password']

#Form to register staff with Person Model
class RegisterStaffForm(ModelForm):
    email = forms.EmailField(max_length=300, widget=forms.EmailInput)
    class Meta:
        model = Person
        fields = ['first_name', 'second_name', 'phone_no', 'email']

#Form to login staff
class LoginStaffAccountForm(ModelForm):
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)
    class Meta:
        model = Account
        fields = ['username', 'password']


