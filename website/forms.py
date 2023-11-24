import datetime
from .models import UserProfile, Booking
from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit
from django.urls import reverse
from django_summernote.widgets import SummernoteWidget
from .models import TABLE_SIZE, TIME_SLOTS


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
        self.helper.layout = Layout(
            Fieldset(
                None,'booking_date', 'booking_time', 'tables_booked', 'additional_info'
            ),
            Submit('submit', 'Submit', css_class='btn btn-secondary btn-brown')
        )           

    # Provides a date widget to the form 
    booking_date = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control', 'type':'date'}), initial=datetime.date.today, required=True)
    booking_time = forms.ChoiceField(choices=TIME_SLOTS, initial=["8:00 - 8:30",], required=True)
    tables_booked = forms.MultipleChoiceField(choices=TABLE_SIZE, initial="Single window seat", required=True)
    additional_info = forms.CharField(max_length=400, widget=SummernoteWidget(), required=False)


    # Provides a model to pull the fields from
    class Meta:
        model = Booking
        fields = ['booking_date', 'booking_time', 'tables_booked', 'additional_info']


    # Prevents booking dates in the past
    def save(self, *args, **kwargs):

        if self.booking_date < datetime.date.today():
            raise ValidationError("The date cannot be in the past!")
        else:
            super(Booking, self).save(*args, **kwargs)




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
    
    
    first_name = forms.CharField(required=True, max_length=50)
    last_name = forms.CharField(required=True, max_length=50)
    phone_number = forms.CharField(required=True, max_length=17)
    email = forms.EmailField(required=True, max_length=300)

    # User data fields
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'phone_number', 'email']
