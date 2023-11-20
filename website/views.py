from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views import generic, View
from .models import Booking


def home(request, template_name="index.html"):
    return render(
        request, template_name
    )

def about(request, template_name="about.html"):
    return render(
        request, template_name,
    )

def booking_form(request, template_name="booking-form.html"):
    return render(
        request, template_name,
    )

@login_required
def user_profile(request, template_name="user-profile"):
    
    profile = request.user.get_profile()

    return render(
        request, template_name,
    )

