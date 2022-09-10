
from django.contrib import admin
from django.urls import path,include

from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('LoginPage/',views.user_login,name='LoginPage'),
    path('logout/',views.user_logout,name="logout"),
    path('signup/',views.signup,name='signup'),
    
    
   
   
    path('no_fund/',views.no_fund,name='no_fund'),

    
    path('forgotPassword/', views.forgotPassword, name='forgotPassword'),
    path('resetpassword_validate/<uidb64>/<token>/', views.resetpassword_validate, name='resetpassword_validate'),
    path('resetPassword/', views.resetPassword, name='resetPassword'),
   
]