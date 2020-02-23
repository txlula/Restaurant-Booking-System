from django.db import models
from django.forms import ModelForm
from django import forms

from phone_field import PhoneField
from datetime import datetime

from django.contrib.auth import authenticate, get_user_model

User = get_user_model()

#Restaurant Model
class Restaurant(models.Model):
    restaurantID = models.AutoField(primary_key=True, unique=True)
    rest_name = models.CharField(max_length=300)
    rest_address = models.TextField()
    rest_phone_no = PhoneField(default="")
    rest_email = models.EmailField(max_length=300, default="")
    rest_max_size = models.PositiveIntegerField()

    #Display information in string format
    def __str__(self):
        return "{}, {}, {}", self.name, self.address, self.phone_no

#Account Model
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

#Reservation Model
class Reservation(models.Model):
    reservationID = models.AutoField(primary_key=True, unique=True)
    no_of_people = models.PositiveIntegerField()
    date_of_booking = models.DateField(default=datetime.now)
    time_of_booking = models.TimeField()
    additional = models.TextField(default="")
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, default="", null=True)

    def __str__(self):
        return "{}, {}, {}", self.no_of_people, self.date_of_booking, self.time_of_booking, self.addtional

    def ValidateDate(self):
        date = self.cleaned_data['date_of_booking']
        if date < datetime.now():
            raise forms.ValidationError("Invalid date")

#Person Model
class Person(models.Model):
    personID = models.AutoField(primary_key=True, unique=True)
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    phone_no = PhoneField(default="")
    email = models.EmailField(max_length=300, unique=True)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, default="", null=True)

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
    order_time = models.DateTimeField()
    order_address = models.TextField()
    #Order model is linked to Dish model
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, default="")

    def __str__(self):
        return "{}, {}", self.order_time, self.order_address

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
        model = Person
        fields = ['first_name', 'second_name', 'phone_no', 'email']

#Form to add dish
class AddDishForm(ModelForm):
    class Meta:
        model = Dish
        fields = ['dish_name', 'dish_price']
        widgets = { 'dish_name' : forms.TextInput(attrs={'placeholder' : 'Dish name'}),
                   'dish_price' : forms.NumberInput(attrs={'placeholder' : 'Price'})
                   }

#Form to login staff
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username = username, password = password)
            if not user:
                raise forms.ValidationError('This user does not exist')
            if user and not user.check_password(password):
                raise forms.ValidationError('The password is incorrect')
        return super(LoginForm, self).clean(*args, **kwargs)

#Form to register staff
class RegisterForm(ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)
    first_name = forms.CharField()
    second_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'second_name', 'email']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        e = User.objects.filter(username = username)
        if e == username:
            raise forms.ValidationError('This username is not available. Try a different one.')
        return username