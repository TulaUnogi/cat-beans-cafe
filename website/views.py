from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import Booking


def home(request):
    return render(request, 'index.html')
