from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()

    class Meta: # gives nested configuration and keeps the configuration in place and 
                #when the user is created it saves into the User model
        model=User
        fields=['username','email','password1','password2']


class UserUpdateForm(forms.ModelForm):
    email=forms.EmailField()

    class Meta: # gives nested configuration and keeps the configuration in place and 
                #when the user is created it saves into the User model
        model=User
        fields=['username','email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['img']