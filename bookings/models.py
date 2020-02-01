from django.db import models
from django.forms import ModelForm
from django import forms

from phone_field import PhoneField

#User Authentication System
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#Restaurant Model
class Restaurant(models.Model):
    #Unique ID for Restaurant, 'AutoField' automatically assigns ID
    restaurantID = models.AutoField(primary_key=True, unique=True)
    rest_name = models.CharField(max_length=300)
    rest_address = models.TextField()
    rest_phone_no = PhoneField()
    rest_max_size = models.PositiveIntegerField()

    #Display information in string format
    def __str__(self):
        return "{}, {}, {}", self.name, self.address, self.phone_no

#Person Model
class Person(models.Model):
    personID = models.AutoField(primary_key=True, unique=True)
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    phone_no = PhoneField()
    email = models.EmailField(max_length=300)

    def __str__(self):
        return "{}, {}, {}, {}", self.first_name, self.second_name, self.phone_no, self.email

#Account Model
class Account(models.Model):
    accountID = models.AutoField(primary_key=True, unique=True)
    #Person model has a one-to-one relationship with User model
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.username

#Reservation Model
class Reservation(models.Model):
    reservationID = models.AutoField(primary_key=True, unique=True)
    no_of_people = models.PositiveIntegerField()
    #Date of reservation
    date_of_booking = models.DateField()
    #Time of reservation, time must be unique
    time_of_booking = models.TimeField(unique=True)

    def __str__(self):
        return "{}, {}, {}", self.no_of_people, self.date_of_booking, self.time_of_booking

#Dish Model
class Dish(models.Model):
	dishID = models.AutoField(primary_key=True, unique=True)
	dish_name = models.CharField(max_length=200)
	dish_price = models.DecimalField(max_digits=5, decimal_places=2)

#Order Model
class Order(models.Model):
    orderID = models.AutoField(primary_key=True, unique=True)
    order_time = models.DateTimeField()
    order_address = models.TextField()
    #Order model is linked to Dish model
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)

    def __str__(self):
        return "{}, {}", self.time, self.address

#Form to reserve with Reservation Model
class ReserveForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ['no_of_people', 'date_of_booking', 'time_of_booking']
        widgets = { 'no_of_people' : forms.NumberInput(attrs={'placeholder' : 'Number of people dining'}), 
                   'date_of_booking' : forms.SelectDateWidget(attrs={'placeholder' : 'Date of booking'}), 
                   'time_of_booking' : forms.DateTimeInput(attrs={'placeholder' : 'Time of booking'}) 
                   }

#Form for customer's input when reserving
class CustomerForm(ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'second_name', 'phone_no', 'email']

#Form to register staff with Python User Authentication System
class RegisterStaffForm(UserCreationForm):
    email = forms.EmailField(max_length=300, widget=forms.EmailInput)
    first_name = forms.CharField(max_length=50)
    second_name = forms.CharField(max_length=50)

    class Meta:
        model = Person
        fields = ['first_name', 'second_name', 'email']

#Form to login staff
class LoginStaffAccountForm(ModelForm):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)
    class Meta:
        model = Account
        fields = ['username', 'password']
        widgets = { 'username' : forms.TextInput(attrs={'placeholder' : 'Username'}),
                   'password' : forms.PasswordInput(attrs={'placeholder' : 'Password'})
                   }

#Form to add dish
class AddDishForm(ModelForm):
    class Meta:
        model = Dish
        fields = ['name', 'price']
        widgets = { 'name' : forms.TextInput(attrs={'placeholder' : 'Dish name'}),
                   'price' : forms.NumberInput(attrs={'placeholder' : 'Price'})
                   }