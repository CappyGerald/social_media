from django import forms
from django.contrib.auth import get_user_model
from .models import Profile

# form for authenticating users against the database
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

# user registration form

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        label='password',
        widget= forms.PasswordInput
    )

    password2 = forms.CharField(
        label='Repeat password',
        widget = forms.PasswordInput
    )
    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'email']

    # checking if the passwords match
    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("passwords Don't match!")
        return cd['password2']
    
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['date_of_birth', 'photo']

class UserEditForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email']

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['date_of_birth', 'photo']