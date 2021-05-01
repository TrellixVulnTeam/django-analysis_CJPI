from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
class SignUpForm(UserCreationForm):
    class Meta:
        model=User
        fields = ('username','first_name','last_name')


class UserProfileForm(forms.ModelForm):
    birth_date=forms.DateField(widget=forms.TextInput(
        attrs={'type':'date'}
    ))
    class Meta:
        model=UserProfile
        # fields='__all__'
        exclude=('user',)