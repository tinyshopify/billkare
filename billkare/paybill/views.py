from email import message
from django.contrib import messages, auth
from django.shortcuts import render
from .forms import UserForm,customer_InfoForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

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



# Create your views here.
def home(request):
    return render(request,"home.html")

@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('home'))
    
def signup(request):

    registered=False

    if request.method == 'POST':

        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        user_form = UserForm(data=request.POST)
        customer_form = customer_InfoForm(data=request.POST)

        # Check to see both forms are valid
        if user_form.is_valid() and customer_form.is_valid():

            # Save User Form to Database
            user = user_form.save()
            user.set_password(user.password)

            user.save()      

            customer = customer_form.save(commit=False)

            # Set One to One relationship between
            # UserForm and customer_InfoForm
            customer.user = user

            
            customer.save()

            # Registration Successful!
            registered = True

        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors,customer_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()
        customer_form = customer_InfoForm()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request,'signup.html',
                          {'user_form':user_form,
                           'customer_form':customer_form,
                           'registered':registered})

    


def user_login(request):
    
    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('form_username')
        password = request.POST.get('form_password')
        
        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)
       
        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                
                return render(request,'Billing_details.html', {'username':username})
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            message="INVALID USERNAME OR PASSWORD"
            return render(request,'LoginPage.html', {'message':message})

    else:
        #Nothing has been provided for username or password.
        return render(request, 'LoginPage.html', {})

     
def Billing_details(request):
    return render(request,"Billing_details.html")

    
def forgotPassword(request):
    if request.method == 'POST':
        email = request.POST['email']
        print(User.objects)
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email__exact=email)
           
            print("hi")
            
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
        user = User._default_manager.get(pk=uid)
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
            user = User.objects.get(pk=uid)
            user.set_password(password)
            user.save()
            messages.success(request, 'Password reset successful')
            return redirect('LoginPage')
        else:
            messages.error(request, 'Password do not match!')
            return redirect('resetPassword')
    else:
        return render(request, 'resetPassword.html')
