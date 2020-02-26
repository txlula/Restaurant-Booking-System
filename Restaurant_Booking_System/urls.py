from bookings import views
from django.contrib import admin
from django.conf.urls import include
from django.urls import path, re_path

from bookings.views import staffregister, stafflogin, stafflogout

urlpatterns = [
    #Admin Page
    path('admin/', admin.site.urls),
    #Start Page
    re_path(r'^$', views.start, name='start'),
    #Register Page
    re_path(r'accounts/register/$', views.staffregister, name='staffregister'),
    #Login Page
    re_path(r'accounts/login/$', views.stafflogin, name='stafflogin'),
    #Logout
    re_path(r'accounts/logout/$', views.stafflogout, name='stafflogout'),
    #Staff Home Page
    re_path(r'staffhome/$', views.staffhome, name='staffhome'),
    #Menu Page
    re_path(r'menu/$', views.menu, name='menu'),
    #Remove Reservation
    path('staffhome/remove/<int:reservation_id>/', views.remove_reservation, name='remove'),
    #Reserve
    path('reserve/<int:restaurant_id>/', views.reserve, name='reserve'),
    #Remove dish
    path(r'menu/remove/<int:dishID>/', views.remove_dish, name='removedish'),
    #Update restaurant information page
    re_path(r'restaurantinfo/$', views.restaurant_info, name='restaurantinfo'),
]
