from django.urls import path

from . import views

urlpatterns = [
    path('no_membership/', views.no_membership, name='no_membership'),
    path('add_membership/',views.add_membership,name='add_membership'),
    path('check_membership/',views.check_membership,name='check_membership'),
    path('cancelmembership/',views.cancelmembership,name='cancelmembership'),
    path('update_membership/',views.update_membership,name='update_membership'),
    path('shortage_membership/',views.shortage_membership,name='shortage_membership'),
    path('subscription/',views.subscription,name='subscription'),
   path('subscription_details/',views.subscription_details,name='subscription_details'),
   
]