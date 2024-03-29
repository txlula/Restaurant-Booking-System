from django.db import models
from django.forms import ModelForm
from django import forms

from phone_field import PhoneField
from datetime import datetime, date
from django.utils import timezone

from django.contrib.auth import authenticate, get_user_model

User = get_user_model()

#Restaurant Model
class Restaurant(models.Model):
    restaurantID = models.AutoField(primary_key=True, unique=True)
    rest_name = models.CharField(max_length=300)
    rest_address = models.TextField()
    rest_phone_no = PhoneField(blank=True, null=True)
    rest_email = models.EmailField(max_length=300, blank=True, null=True)
    rest_max_size = models.PositiveIntegerField(default=0)
    rest_menu = models.ImageField(upload_to = 'menus', null=True, blank=True)

    #Display information in string format
    def __str__(self):
        return "{}, {}, {}", self.name, self.address, self.phone_no

#Account Model
class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, default="")

    def __str__(self):
        return self.user.username

#Reservation Model
class Reservation(models.Model):
    reservationID = models.AutoField(primary_key=True, unique=True)
    no_of_people = models.PositiveIntegerField()
    date_of_booking = models.DateField(default=datetime.now)
    time_of_booking = models.TimeField()
    additional = models.TextField(blank=True, null=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, default="", null=True)

    def __str__(self):
        return "{}, {}, {}", self.no_of_people, self.date_of_booking, self.time_of_booking, self.addtional

#Person Model
class Customer(models.Model):
    customerID = models.AutoField(primary_key=True, unique=True)
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    phone_no = PhoneField(blank=True, null=True)
    email = models.EmailField(max_length=300, unique=True, null=True)
    reservation = models.OneToOneField(Reservation, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return "{}, {}, {}, {}", self.first_name, self.second_name, self.phone_no, self.email

#Dish Model
class Dish(models.Model):
	dishID = models.AutoField(primary_key=True, unique=True)
	dish_name = models.CharField(max_length=200)
	dish_price = models.DecimalField(max_digits=5, decimal_places=2)

#Order Model
class Order(models.Model):
    orderID = models.AutoField(primary_key=True, unique=True)
    order_date = models.DateField(default=date.today)
    order_time = models.DateTimeField(auto_now_add=True)
    order_address = models.TextField()
    #Order model is linked to Dish model
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return "{}, {}", self.order_time, self.order_address

#Form to search up restaurant
class SearchRestaurantForm(forms.Form):
    restaurant_name = forms.CharField()

#Form to reserve with Reservation Model
class ReserveForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ['no_of_people', 'date_of_booking', 'time_of_booking', 'additional']
        widgets = { 'no_of_people' : forms.NumberInput(attrs={'placeholder' : 'Number of people dining'}), 
                   'date_of_booking' : forms.SelectDateWidget(attrs={'placeholder' : 'Date of booking'}), 
                   'time_of_booking' : forms.TimeInput(attrs={'placeholder' : 'Time of booking'}),
                   'additional' : forms.Textarea(attrs={'placeholder' : 'Additional information'})
                   }

#Form for customer's input when reserving
class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'second_name', 'phone_no', 'email']

#Form to add dish
class AddDishForm(ModelForm):
    class Meta:
        model = Dish
        fields = ['dish_name', 'dish_price']
        widgets = { 'dish_name' : forms.TextInput(attrs={'placeholder' : 'Dish name'}),
                   'dish_price' : forms.NumberInput(attrs={'placeholder' : 'Price'})
                   }

#Form to upload menu file
class AddMenuFile(ModelForm):
    class Meta:
        model = Restaurant
        fields = ['rest_menu']
        widgets = {'rest_menu' : forms.ClearableFileInput(attrs={'multiple': True})}

#Form to login staff
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)

#Form to register staff
class RegisterForm(ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)
    first_name = forms.CharField()
    second_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'second_name', 'email']

#Form to input information for restaurant
class RestaurantInfoForm(ModelForm):
    class Meta:
        model = Restaurant
        fields = ['rest_name', 'rest_address', 'rest_phone_no', 'rest_email', 'rest_max_size', 'rest_menu']
        widgets = {'rest_name' : forms.TextInput(attrs={'placeholder' : 'Restaurant name'}),
                 'rest_address' : forms.Textarea(attrs={'placeholder' : 'Restaurant address'}),
                 }