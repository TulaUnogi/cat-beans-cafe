from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views import generic, View
from .models import Booking, UserProfile
from website.forms import BookingForm, ProfileForm
from django.contrib import messages
from django.contrib.auth.models import User


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

@login_required
def edit_profile(request):

    user = get_object_or_404(User, id=request.user.id)
    template_name = 'edit-profile.html'

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = user
            instance.save(commit=True)
            messages.success(request, 'Thank you! Your profile has been updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Make sure you filled up all the required fields properly!')
            return redirect('profile')
    else:
        form = ProfileForm()

    return render(request, template_name, {'form': form})

@login_required
def delete_account(request):

    user = get_object_or_404(User, id=request.user.id)

    try:
        user.delete()
        messages.success(request, 'Your account has been deleted successfully!')
        return redirect('home')
    except Exception as e: 
        messages.error(request, 'Oops! Something went wrong!')
        return redirect('home')
    