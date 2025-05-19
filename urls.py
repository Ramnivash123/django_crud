"""
URL configuration for django_user project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from user.views import adduser, index, userinfo, addstate, addcity, userinfo, stateinfo, cityinfo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('adduser/', adduser),  # Use your view here
    path('addstate/', addstate),  # Use your view here
    path('addcity/', addcity),
    path('userinfo/', userinfo),  # Use your view here
    path('stateinfo/', stateinfo),  # Use your view here
    path('cityinfo/', cityinfo),  # Use your view here
]
