"""
Restaurant_Booking_System URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/

Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Uncomment next two lines to enable admin:
from bookings import views
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, re_path, include
#from bookings.views import loginscreen, home, register

urlpatterns = [
    # Uncomment the next line to enable the admin:
    path('admin/', admin.site.urls),
    re_path(r'^$', views.start, name='start'),
    re_path(r'stafflogin/$', views.staffloginscreen, name='stafflogin'),
    re_path(r'staffregister/$', views.staffregister, name='staffregister'),
    re_path(r'staffhome/$', views.staffhome, name='staffhome'),
    re_path(r'content/$', views.content, name='content'),
]
