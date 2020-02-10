from django.db import models
from django.forms import ModelForm
from django import forms

from phone_field import PhoneField
from datetime import datetime

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#Restaurant Model
class Restaurant(models.Model):
    restaurantID = models.AutoField(primary_key=True, unique=True)
    rest_name = models.CharField(max_length=300)
    rest_address = models.TextField()
    rest_phone_no = PhoneField(default="")
    rest_max_size = models.PositiveIntegerField()

    #Display information in string format
    def __str__(self):
        return "{}, {}, {}", self.name, self.address, self.phone_no

#Person Model
class Person(models.Model):
    personID = models.AutoField(primary_key=True, unique=True)
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    phone_no = PhoneField(default="")
    email = models.EmailField(max_length=300)

    def __str__(self):
        return "{}, {}, {}, {}", self.first_name, self.second_name, self.phone_no, self.email

#Account Model
class Account(models.Model):
    accountID = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username

#Reservation Model
class Reservation(models.Model):
    no_of_people = models.PositiveIntegerField()
    date_of_booking = models.DateField(default=datetime.now)
    time_of_booking = models.TimeField()
    person = models.OneToOneField(Person, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return "{}, {}, {}", self.no_of_people, self.date_of_booking, self.time_of_booking

    def ValidateDate(self):
        date = self.cleaned_data['date_of_booking']
        if date < datetime.now():
            raise forms.ValidationError("Invalid date")

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
        return "{}, {}", self.order_time, self.order_address

#Form to search up restaurant by name


#Form to reserve with Reservation Model
class ReserveForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ['no_of_people', 'date_of_booking', 'time_of_booking']
        widgets = { 'no_of_people' : forms.NumberInput(attrs={'placeholder' : 'Number of people dining'}), 
                   'date_of_booking' : forms.SelectDateWidget(attrs={'placeholder' : 'Date of booking'}), 
                   'time_of_booking' : forms.TimeInput(attrs={'placeholder' : 'Time of booking'}) 
                   }

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
        widgets = { 'username' : forms.TextInput(attrs={'placeholder' : 'Username'}),
                   'password' : forms.PasswordInput(attrs={'placeholder' : 'Password'})
                   }

#Form to register staff with Python User Authentication System
class RegisterStaffForm(UserCreationForm):
    email = forms.EmailField(max_length=300, widget=forms.EmailInput)
    first_name = forms.CharField(max_length=50)
    second_name = forms.CharField(max_length=50)

    class Meta:
        model = User
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
        fields = ['dish_name', 'dish_price']
        widgets = { 'dish_name' : forms.TextInput(attrs={'placeholder' : 'Dish name'}),
                   'dish_price' : forms.NumberInput(attrs={'placeholder' : 'Price'})
                   }