from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Restaurant)
admin.site.register(Reservation)
admin.site.register(Staff)
admin.site.register(Order)
admin.site.register(Dish)