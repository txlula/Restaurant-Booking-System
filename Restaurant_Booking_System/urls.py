from bookings import views
from django.contrib import admin
from django.conf.urls import url
from django.conf.urls import include
from django.urls import path, re_path

from bookings.views import staffregister, stafflogin, stafflogout

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', views.start, name='start'),
    re_path(r'accounts/register/$', views.staffregister, name='staffregister'),
    re_path(r'accounts/login/$', views.stafflogin, name='stafflogin'),
    re_path(r'accounts/logout/$', views.stafflogout, name='stafflogout'),
    re_path(r'staffhome/$', views.staffhome, name='staffhome'),
    re_path(r'menu/$', views.menu, name='menu'),
    path('stafflogin/staffhome/remove/<int:reservation_id>/', views.remove_reservation, name='remove'),
    path('reserve/<int:restaurant_id>/', views.reserve, name='reserve'),
]
