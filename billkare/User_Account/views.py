
from django.contrib import messages

from django.shortcuts import render

from Loan.models import SLTLoan
from .forms import AuthForm,LoginForm
from Loan.forms import SLTLoanForm
from .models import SLTAuth,SLTLogin
from . import function
from Loan import views

from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
# import csv,os,json
# from billkare.settings import Filepath

# Extra Imports for the Login and Logout Capabilities
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Verification email
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage


def home(request):
    
    logout(request)
    return render(request,"home.html")

@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('home'))

def no_fund(request):
   return render(request,"no_fund.html")
   




def signup(request):

    registered=False
    print(request.method)
    if request.method == 'POST':
        # It appears as one form to the user on the .html page
        user_form =AuthForm(data=request.POST)
        bankname=request.POST.get('bank_list')
        
        if user_form.is_valid():
                user = user_form.save(commit=False)
                user.set_password(user.password)
                user.sal_bname=bankname
                user.save()  
                new_user = authenticate(email=user_form.cleaned_data['email'],
                                    password=user_form.cleaned_data['password'],
                                    )
                login(request, new_user)    
                 #Registration Successful!
                registered = True
                messages.success(request, 'Cathe signup succcessfully!.')
                return redirect('connect_bank')

        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = AuthForm()

    return render(request,'signup.html',
                          {'user_form':user_form,
                           'registered':registered})

def user_login(request):
    if request.user.is_authenticated:
        logout(request)
    login_form=LoginForm()
    if request.method == 'POST':
        login_form=LoginForm(data=request.POST)
        email = request.POST.get('user_email')
        password = request.POST.get('password')
        # bankname=request.POST.get('bank_list')
  
        
        # Django's built-in authentication function:
        user = authenticate(email=email,password=password)
        print(user)
        if login_form.is_valid():
        # If we have a user
            if user:
                #Check it the account is active
                if user.is_active:
                    user1 = SLTLogin()
                    user1.user_email=email
                    # user1.salary_bankname=bankname
                    user1.save()
                    # Log the user in.
                    login(request,user)
                    return redirect('transaction_details')
                
                else:
                    # If account is not active:
                    return HttpResponse("Your account is not active.")
            else:
                print("Someone tried to login and failed.")
                print("They used username: {} and password: {}".format(email,password))
                messages.error(request, 'Invalid username or password.')
                return render(request,'LoginPage.html',{'login_form':login_form})
        else:
            # One of the forms was invalid if this else gets called.
            print(login_form.errors)

    else:
       
        return render(request, 'LoginPage.html', {'login_form':login_form})

     


    
def forgotPassword(request):
    if request.method == 'POST':
        email = request.POST['email']
        
        if SLTAuth.objects.filter(email=email).exists():
            user = SLTAuth.objects.get(email__exact=email)            
            # Reset password email
            current_site = get_current_site(request)
            mail_subject = 'Reset Your Password'
            
            message = render_to_string('reset_password_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()

            messages.success(request, 'Password reset email has been sent to your email address.')
            return redirect('forgotPassword')
        else:
            messages.error(request, 'Account does not exist!')
            print("no account")
            return redirect('forgotPassword')
    return render(request, 'forgotPassword.html')


def resetpassword_validate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = SLTAuth._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        messages.success(request, 'Please reset your password')
        return redirect('resetPassword')
    else:
        messages.error(request, 'This link has been expired!')
        return redirect('LoginPage')


def resetPassword(request):
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            uid = request.session.get('uid')
            user = SLTAuth.objects.get(pk=uid)
            user.set_password(password)
            user.save()
            messages.success(request, 'Password reset successful')
            return redirect('LoginPage')
        else:
            messages.error(request, 'Password do not match!')
            return redirect('resetPassword')
    else:
        return render(request, 'resetPassword.html')

