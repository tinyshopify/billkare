from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from . import common
from User_Account import function
# from .models import User
from User_Account.models import SLT_accesstocken,SLTAuth
from django.urls import reverse
from django.contrib.auth.decorators import login_required


from django.views.decorators.csrf import csrf_protect, csrf_exempt
import json
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie

# Create your views here.

import plaid
from plaid.api import plaid_api
from .secret_keys import PLAID_CLIENT_ID, PLAID_SECRET
from plaid.model.item_public_token_exchange_request import ItemPublicTokenExchangeRequest

configuration = plaid.Configuration(
    host=plaid.Environment.Sandbox,
    api_key={
        'clientId': PLAID_CLIENT_ID,
        'secret': PLAID_SECRET,
    }
)

api_client = plaid.ApiClient(configuration)
client = plaid_api.PlaidApi(api_client)

def user_creation(request):
    
        if request.user.is_authenticated:
         user_id = str(function.get_user(request.user.email))
         print(user_id)
        link_token = common.get_link_token(user_id)
        return redirect('plaidlink:get_plaid_link', link_token=link_token)
   



def get_plaid_link(request, link_token):
    print(request.user.first_name)
    return render(request, template_name='plaidlink/plaid_api.html', context={'link_token': link_token})


@ensure_csrf_cookie
def create_link_token(request, username):
    link_token = common.get_link_token(username)
    print(link_token)
    return render(link_token, safe=False)


def exchange_public_token(request, public_token):
    
    id=function.get_user(request.user.email)
    
    global access_token
    request = ItemPublicTokenExchangeRequest(
        public_token=public_token
    )
    response = client.item_public_token_exchange(request)
    
    access_token = response['access_token']
    item_id = response['item_id']
    
    print('success')
    SLT_accesstocken.objects.update_or_create(SLT_id_id=id,access_token=access_token)
   
    print("access_token:" + access_token)
    return HttpResponseRedirect(reverse('home'))


