from django.urls import include, path
from django.contrib import admin
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('booking/', views.booking_form, name='booking'),
    path('my-profile/', views.user_profile, name='profile'),
    path('edit-profile/', views.edit_profile, name='editprofile'),
    path('delete-account/', views.delete_account, name='deleteaccount'),
    path('edit-booking/<slug:slug>', views.EditBooking.as_view(), name='editbooking'),
    path('delete-booking/', views.delete_booking, name='deletebooking'),
]
