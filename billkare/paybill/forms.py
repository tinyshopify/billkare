from django import forms
from django.contrib.auth.models import User
from .models import customer_Info

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
   
    class Meta():
        model = User
        fields = ('username','email','password')


class customer_InfoForm(forms.ModelForm):
    class Meta():
        model = customer_Info
        fields =('customer_phonenumber',)


