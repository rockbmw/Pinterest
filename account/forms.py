from django import forms
from django.contrib.auth.models import User

from .models import Profile

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput
    )    
    password2 = forms.CharField(
        label='Repeat password',
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ('username','first_name','email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords do not match')
        return cd['password2']

    
class UserEditForm(forms.ModelForm):
    """
    Form to allow the user to edit their first_name,
    last_name, and email.
    """
    
    class Meta:
        model = User
        fields = ('first_name','last_name','email')

class ProfileEditForm(forms.ModelForm):
    """
    Form to let the user edit his profile. This is 
    extra data saved in custom Profile model.
    """
    
    class  Meta:
        model = Profile
        fields = ('date_of_birth','photo')