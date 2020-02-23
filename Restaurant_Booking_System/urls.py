from bookings import views
from django.contrib import admin
from django.conf.urls import url
from django.conf.urls import include
from django.urls import path, re_path

from bookings.views import staffregister, stafflogin, stafflogout

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', views.start, name='start'),
    path('accounts/register/', staffregister),
    path('accounts/login/', stafflogin),
    path('accounts/logout/', stafflogout),
    re_path(r'staffhome/$', views.staffhome, name='staffhome'),
    re_path(r'menu/$', views.menu, name='menu'),
    path('stafflogin/staffhome/remove/<int:reservation_id>/', views.remove_reservation, name='remove'),
    path('reserve/<int:restaurant_id>/', views.reserve, name='reserve'),
]
