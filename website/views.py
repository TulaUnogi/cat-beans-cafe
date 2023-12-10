from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views import generic, View
from django.views.generic.edit import UpdateView
from .models import Booking, UserProfile
from website.forms import BookingForm, ProfileForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin


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


class EditBooking(UpdateView, LoginRequiredMixin):

    model = Booking
    form_class = BookingForm   
    template_name = 'edit-booking.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        form.instance.booking_customer = UserProfile.objects.get(
            user=self.request.user
        )
        messages.success(self.request, 'Thank you! Your booking has been updated!')
        return super().form_valid(form)


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
    