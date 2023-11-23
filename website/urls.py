from django.urls import include, path
from django.contrib import admin
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('booking/', views.booking_form, name='booking'),
    path('my-profile/', views.user_profile, name='profile'),
]
