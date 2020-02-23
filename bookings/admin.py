from django.contrib import admin

from .models import *

admin.site.register(Restaurant)
admin.site.register(Reservation)
admin.site.register(Person)
admin.site.register(Dish)
admin.site.register(Order)
admin.site.register(Account)