from django.urls import path

from . import views
app_name = 'plaidlink'
urlpatterns = [
    path('', views.user_creation, name='index'),
    path('get_plaid_link/<link_token>', views.get_plaid_link, name='get_plaid_link'),
    path('exchange_public_token/<public_token>', views.exchange_public_token, name='exchange_public_token'),
]