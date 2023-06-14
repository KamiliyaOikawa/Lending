from captcha.fields import ReCaptchaField
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import MyUser, Profile


class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


class RegistrationForm(UserCreationForm):
    username = forms.CharField(label='Username')
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    captcha = ReCaptchaField()

    class Meta(UserCreationForm.Meta):
        model = MyUser
        fields = ['username', 'email', 'password1', 'password2', 'captcha']

    def clean_email(self):
        email = self.cleaned_data['email']
        if MyUser.objects.filter(email=email).exists():
            raise forms.ValidationError('This email address is already in use.')
        return email


""" Form for Profile of the User """


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo', 'name', 'telegram', 'email', 'additional_info']