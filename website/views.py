from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views import generic, View
from .models import Booking, UserProfile
from website.forms import BookingForm, ProfileForm
from django.contrib import messages


def home(request, template_name="index.html"):
    return render(
        request, template_name
    )

def about(request, template_name="about.html"):
    return render(
        request, template_name,
    )


@login_required     
def booking_form(request):

    template_name = 'booking-form.html'
    form = BookingForm(data=request.POST)

    if request.method == 'POST':        
        
        if form.is_valid():
            booking = form.save(commit=False)
            customer_data = UserProfile.objects.all()
            booking.customer = customer_data
            booking.save(commit=True)
            messages.success(request, 'Thank you! Your booking has been saved! You can access it through "My Bookings" page.')
            return redirect('home')
        else:
            messages.error(request, 'Please make sure to fill up all the necessary fields!')
            return redirect(booking_form)

    return render(
                request, template_name, {'form': form},
                )

            
@login_required
def user_profile(request):
    
    customer_data = UserProfile.objects.all()
    my_bookings = Booking.objects.all()

    template_name = 'user-profile.html'

    return render(
                request, template_name, {'profile': customer_data, 'bookings': my_bookings}
                )


