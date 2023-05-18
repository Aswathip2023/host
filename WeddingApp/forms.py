from django.contrib.admin.widgets import AdminDateWidget
# from django_datetimepicker.widgets import TimeWidget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth import get_user_model
from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Booking
from django.forms import ModelForm, TimeInput
from WeddingApp import models


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(help_text='', required=True)

    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        help_texts = {

            'first_name': None,
            'last_name': None,
            'email': None,
            'password1': None,
            'password2': None,
        }

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

    def clean(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email exists")
        return self.cleaned_data
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

class DateInput(forms.DateInput):
    input_type = 'date'


class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        exclude = ['user']
        fields = '__all__'
        widgets = {
            'booking_date': DateInput(),
            # 'check_in': forms.TimeField(widget=forms.TimeInput(format='%H:%M')),
            # 'check_out': forms.TimeField(widget=forms.TimeInput(format='%H:%M')),
        }

        labels = {
            'name':"Service",
            'contact': "Contact Number: ",
            'booking_date': "Booking Date: ",
            'check_in': "Check-In Time:",
            'check_out': "Check-Out Time:",
            'count': "No:of members:",
            'description': "Description:",
        }

