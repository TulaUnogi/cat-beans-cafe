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
    slug = form.slug

    if request.method == 'POST':        
        
        if form.is_valid():
            
            booking = form.save(commit=False)
            customer_data = get_object_or_404(UserProfile, user=request.user)
            booking.booking_customer = customer_data
            booking_id = booking.id
            booking.save()
            messages.success(request, 'Thank you! Your booking has been saved! You can access it through "My Bookings" page.')
            return redirect('home')
        else:
            messages.error(request, form.errors)
            return redirect(booking_form)

    return render(
                request, template_name, {'form': form},
                )


@login_required
def edit_booking(request):       
    
    template_name = 'edit-profile.html'
    my_bookings = Booking.objects.filter(booking_customer=request.user.userprofile)
    customer_data = UserProfile.objects.all()
    booking = get_object_or_404(my_bookings)

    if request.user.is_authenticated:
        booking = get_object_or_404(Booking, id=booking_id)
        if request.method == 'POST':
            form = BookingForm(request.POST, instance=booking)
            
            if form.is_valid():
                instance = form.save(commit=False)
                instance.customer_data = customer_data
                instance.save()
                messages.success(request, 'Thank you! Your profile has been updated!')
            else:
                return messages.error(request, form.errors)

    else:
        initial_data = {}
        form = BookingForm(initial={
                'booking_date': booking.booking_date,
                'booking_time': booking.booking_time,
                'table_size': booking.table_size,
                'additional_info': booking.additional_info,                    
            })
    return render(request, template_name, {'form': form})


@login_required
def delete_booking(request):
    pass
            
@login_required
def user_profile(request):
    
    customer_data = UserProfile.objects.all()
    my_bookings = Booking.objects.filter(booking_customer=request.user.userprofile)

    template_name = 'user-profile.html'

    return render(
                request, template_name, {'profile': customer_data, 'bookings': my_bookings}
                )


@login_required
def edit_profile(request):

    template_name = 'edit-profile.html'
    customer_data = UserProfile.objects.all()

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.userprofile)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.customer_data = customer_data
            instance.save()
            messages.success(request, 'Thank you! Your profile has been updated!')
            return redirect('profile')
        else:
            messages.error(request, form.errors)
            return redirect('profile')
    else:
        profile = get_object_or_404(UserProfile, user=request.user)
        initial_data = {}
        if profile.user:
            form = ProfileForm(initial={
                    'first_name': profile.first_name,                    
                    'last_name': profile.last_name,
                    'phone_number': profile.phone_number,
                    'email': request.user.email,                    
                })

    return render(request, template_name, {'form': form})

@login_required
def delete_account(request):

    user = get_object_or_404(User, id=request.user.id)
    profile = UserProfile.objects.all()

    try:
        profile.delete()
        user.delete()
        messages.success(request, 'Your account has been deleted successfully!')
        return redirect('home')
    except Exception as e: 
        messages.error(request, 'Oops! Something went wrong!')
        return redirect('home')
    