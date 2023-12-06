import datetime
from django.utils.timezone import now
from .models import UserProfile, Booking
from django import forms
from django.forms import ModelForm, CheckboxSelectMultiple, TextInput, NumberInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django_summernote.widgets import SummernoteWidget
from .models import TABLE_SIZE, TIME_SLOTS
from autoslug import AutoSlugField

class BookingForm(ModelForm):
    """ 
    Provides necessary fields to the booking form for customers
    """

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        # Crispy form helpers
        self.helper = FormHelper()
        self.helper.form_method = 'post'        
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn btn-secondary btn-brown mb-4 mx-auto px-5'))        

    # Provides a date widget to the form 
    booking_date = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control', 'type':'date', 'value': datetime.date.today}), required=False)
    booking_time = forms.ChoiceField(choices=TIME_SLOTS, required=False)
    table_size = forms.ChoiceField(choices=TABLE_SIZE, required=False)
    additional_info = forms.CharField(max_length=400, widget=SummernoteWidget(), required=False)
    booked_on = forms.DateTimeField(initial=datetime.datetime.now, widget=forms.HiddenInput(), required = False)
    slug = AutoSlugField(max_length=70, unique=True, populate_from=lambda instance: instance.title,
                         unique_with=['booked_on', 'booking_date'],
                         slugify=lambda value: value.replace(' ','-')) 


    # Provides a model to pull the fields from
    class Meta:
        model = Booking
        fields = ['booking_date', 'booking_time', 'table_size', 'additional_info']
        read_only = ['booked_on', 'slug']


    # Prevents booking dates in the past
    def save_booking(self, *args, **kwargs):

        data = self.cleaned_data
        if data.get('booking_date') < datetime.date.today():        
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
    
        
        first_name = forms.CharField(required=True, max_length=50, widget=TextInput(attrs={'autocomplete': 'given-name',}))
        last_name = forms.CharField(required=True, max_length=50, widget=TextInput(attrs={'autocomplete': 'family-name',}))
        phone_number = forms.IntegerField(required=True, widget=NumberInput(attrs={'autocomplete': 'tel',}))
        email = forms.EmailField(required=True, max_length=300, widget=TextInput(attrs={'autocomplete': 'email',}))

    def profile_data(self, request, user):

        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.phone_number = self.cleaned_data['phone_number']
        user.email = self.cleaned_data['email']

        user.save(commit=True)

    # User data fields
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'phone_number', 'email']
