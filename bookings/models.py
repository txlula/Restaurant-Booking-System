from django.db import models
#'ModelForm' is imported to link forms to models
from django.forms import ModelForm
from django import forms

#Restaurant Model
class Restaurant(models.Model):
    #Unique ID for Restaurant, 'AutoField' automatically assigns ID
    restaurantID = models.AutoField(primary_key=True, unique=True)
    #Restaurant's name, maximum characters = 300
    name = models.CharField(max_length=300)
    #Restaurant's address
    address = models.TextField()
    #Restaurant's phone number, integer must be positive
    phone_no = models.PositiveIntegerField()
    #Restaurant's maximum size, integer must be positive
    max_size = models.PositiveIntegerField()

    #Display information in string format
    def __str__(self):
        return "{}, {}, {}", self.name, self.address, self.phone_no

#Person Model
class Person(models.Model):
    #Unique ID for Person
    personID = models.AutoField(primary_key=True, unique=True)
    #First Name, maximum characters = 50
    first_name = models.CharField(max_length=50)
    #Second Name, maximum characters = 50
    second_name = models.CharField(max_length=50)
    #Phone Number, integer must be positive
    phone_no = models.PositiveIntegerField()
    #Email, must be in email format, maximum characters = 300
    email = models.EmailField(max_length=300)

    #Display information in string format
    def __str__(self):
        return "{}, {}, {}, {}", self.first_name, self.second_name, self.phone_no, self.email

#Account Model
class Account(models.Model):
    #Unique ID for Account
    accountID = models.AutoField(primary_key=True, unique=True)
    #Username, maximum characters = 20
    username = models.CharField(max_length=20)
    #Password, maximum characters = 20
    password = models.CharField(max_length=20)

    #Display information in string format
    def __str__(self):
        return self.username

#Reservation Model
class Reservation(models.Model):
    #Unique ID for Reservation
    reservationID = models.AutoField(primary_key=True, unique=True)
    #Number of people, integer must be positive
    no_of_people = models.PositiveIntegerField()
    #Date of reservation
    date_of_booking = models.DateField()
    #Time of reservation, time must be unique
    time_of_booking = models.TimeField(unique=True)

    #Display information in string format
    def __str__(self):
        return "{}, {}, {}", self.no_of_people, self.date_of_booking, self.time_of_booking

#Dish Model
class Dish(models.Model):
    #Unique ID for Dish
	dishID = models.AutoField(primary_key=True, unique=True)
    #Dish Name, maximum characters = 200
	name = models.CharField(max_length=200)
    #Dish price
	price = models.DecimalField(max_digits=5, decimal_places=2)


#Order Model
class Order(models.Model):
    #Unique ID for Order
    orderID = models.AutoField(primary_key=True, unique=True)
    #Time of order
    time = models.DateTimeField()
    #Address that it will delievered to
    address = models.TextField()
    #Order model is linked to Dish model
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

#Form to add dish
class AddDishForm(ModelForm):
    class Meta:
        model = Dish
        fields = ['name', 'price']
        widgets = { 'name' : forms.TextInput(attrs={'placeholder' : 'Dish name'}),
                   'price' : forms.NumberInput(attrs={'placeholder' : 'Price'})
                   }