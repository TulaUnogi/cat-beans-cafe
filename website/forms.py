from .models import UserProfile, Booking
from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.urls import reverse


class BookingForm(ModelForm):
    """ 
    Provides necessary fields to the booking form for customers
    """
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        # Crispy form helpers
        self.helper = FormHelper()
        self.helper.form_class = 'brown-inputs'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

    # Provides a date widget to the form 
    booking_date = forms.DateField(widget=forms.DateInput, required=True)


    # Provides a model to pull the fields from
    class Meta:
        model = Booking
        fields = ['booking_date', 'booking_time', 'tables_booked', 'additional_info']


class ProfileForm(ModelForm):
    """ 
    Provides required User data for User profile
    """

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        # Crispy form helpers
        self.helper = FormHelper()
        self.helper.form_class = 'brown-inputs'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))
    

    # User data fields
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'phone_number', 'email']
