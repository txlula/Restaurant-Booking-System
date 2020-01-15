from bookings import views
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', views.start, name='start'),
    re_path(r'stafflogin/$', views.staffloginscreen, name='stafflogin'),
    re_path(r'staffregister/$', views.staffregister, name='staffregister'),
    re_path(r'staffhome/$', views.staffhome, name='staffhome'),
    re_path(r'reserve/$', views.reserve, name='reserve'),
]
