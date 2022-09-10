from django import forms
from django.forms.widgets import HiddenInput
from .models import SLTAuth,SLTLogin

class AuthForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    # bank_list=forms.ModelChoiceField(label=('Select your Salary bank'),queryset=BANKCHOICES.objects.all(),empty_label="(Select here)",
    # to_field_name="bank_choices", widget = forms.Select(attrs = {'onchange' : "myFunction(this.value)"}))
    class Meta():
        model = SLTAuth
        fields = ('email','password','first_name','last_name','phone_number',)
        
    def __init__(self, *args, **kwargs):
        super( AuthForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        self.fields['phone_number'].widget.attrs['placeholder'] = ' Phone Number'
        self.fields['email'].widget.attrs['placeholder'] = ' Email Address'
        
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].widget.attrs['size'] = "width:500px"

    #          password validators
    #   -----------------------------------------
    # def clean(self):
    #     cleaned_data = super(AuthForm, self).clean()
    #     password = cleaned_data.get('password')

    #     # check for min length
    #     min_length = 8
    #     if len(password) < min_length:
    #         msg = 'Password must be at least %s characters long.' % (str(min_length))
    #         self.add_error('password', msg)

    #     # check for digit
    #     if sum(c.isdigit() for c in password) < 1:
    #         msg = 'Password must contain at least 1 number.'
    #         self.add_error('password', msg)

    #     # check for uppercase letter
    #     if not any(c.isupper() for c in password):
    #         msg = 'Password must contain at least 1 uppercase letter.'
    #         self.add_error('password', msg)

    #     if not any(char.isalpha() for char in password):
    #         self.add_error('password', 'Password must contain at letters.')

class LoginForm(forms.ModelForm):
     password = forms.CharField(widget=forms.PasswordInput())
    #  bank_list=forms.ModelChoiceField(queryset=BANKCHOICES.objects.all(),empty_label="(Select here)",
    #  to_field_name="bank_choices")
     
     class Meta():
        model = SLTLogin
        fields = ('user_email','password')
        
     def __init__(self, *args, **kwargs):
        super( LoginForm, self).__init__(*args, **kwargs)
        
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

