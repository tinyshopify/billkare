from django.urls import path

from . import views

urlpatterns = [
    path('no_membership/', views.no_membership, name='no_membership'),
    path('add_membership/',views.add_membership,name='add_membership'),
    path('check_membership/',views.check_membership,name='check_membership'),
   
   
]