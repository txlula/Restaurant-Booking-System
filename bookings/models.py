from django.db import models
from django.forms import ModelForm
from django import forms

#Restaurant Model
class Restaurant(models.Model):
    restaurantID = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=300)
    address = models.TextField()
    phone_no = models.PositiveIntegerField()
    max_size = models.PositiveIntegerField()

    #Display information in string format
    def __str__(self):
        return "{}, {}, {}", self.name, self.address, self.phone_no

#Person Model
class Person(models.Model):
    personID = models.AutoField(primary_key=True, unique=True)
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    phone_no = models.PositiveIntegerField()
    email = models.EmailField(max_length=300)

    #Display information in string format
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
    reservationID = models.AutoField(primary_key=True, unique=True)
    no_of_people = models.PositiveIntegerField()
    date_of_booking = models.DateField()
    time_of_booking = models.TimeField(unique=True)

    #Display information in string format
    def __str__(self):
        return "{}, {}, {}", self.no_of_people, self.date_of_booking, self.time_of_booking

#Dish Model
class Dish(models.Model):
	dishID = models.AutoField(primary_key=True, unique=True)
	name = models.CharField(max_length=200)
	price = models.DecimalField(max_digits=5, decimal_places=2)

#Order Model
class Order(models.Model):
    orderID = models.AutoField(primary_key=True, unique=True)
    time = models.DateTimeField()
    address = models.TextField()
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)

    #Display information in string format
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

#Form to register staff with Account Model
class RegisterStaffAccountForm(ModelForm):
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)
    class Meta:
        model = Account
        fields = ['username', 'password']
        widgets = { 'username' : forms.TextInput(attrs={'placeholder' : 'Username'}),
                   'password' : forms.PasswordInput(attrs={'placeholder' : 'Password'})
                   }

#Form to register staff with Person Model
class RegisterStaffForm(ModelForm):
    email = forms.EmailField(max_length=300, widget=forms.EmailInput)
    class Meta:
        model = Person
        fields = ['first_name', 'second_name', 'phone_no', 'email']
        widgets = { 'first_name' : forms.TextInput(attrs={'placeholder' : 'First Name'}),
                   'second_name' : forms.TextInput(attrs={'placeholder' : 'Second Name'}),
                   'phone_no' : forms.NumberInput(attrs={'placeholder' : 'Phone Number'}),
                   'email' : forms.EmailInput(attrs={'placeholder' : 'Email'})
                   }

#Form to login staff
class LoginStaffAccountForm(ModelForm):
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)
    class Meta:
        model = Account
        fields = ['username', 'password']
        widgets = { 'username' : forms.TextInput(attrs={'placeholder' : 'Username'}),
                   'password' : forms.PasswordInput(attrs={'placeholder' : 'Password'})
                   }