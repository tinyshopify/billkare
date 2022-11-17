from django.shortcuts import render,redirect
import datetime
from datetime import date
from Loan.models import customer_loan_decision_attrs_active
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from . import common

from User_Account import function
# from .models import User
from .models import plaidUser

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

time=datetime.datetime.utcnow().strftime('%H:%M:%S')
dt=datetime.datetime.utcnow()


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
    
    return render(request, template_name='plaidlink/plaid_api.html', context={'link_token': link_token})


@ensure_csrf_cookie
def create_link_token(request, username):
    link_token = common.get_link_token(username)
    print(link_token)
    return render(link_token, safe=False)


def exchange_public_token(request, public_token):
    
    id=function.get_user(request.user.email)
    username=request.user.first_name
    global access_token
    request = ItemPublicTokenExchangeRequest(
        public_token=public_token
    )
    response = client.item_public_token_exchange(request)
    
    access_token = response['access_token']
    item_id = response['item_id']
    
    print("bank connection success")
    plaidUser.objects.update_or_create(
         Sugan_id_id=id,
         access_token=access_token,
          creUser=username,
          CreatedTs = dt,
          UpdateTs =dt,
          InsUpdFlag ="I",)
   
    print("access_token:" + access_token)
    common.insertPlaidHistory(id,username)
    print("history Updated")

    obj=plaidUser.objects.get(Sugan_id_id=id)
    accessToken=obj.access_token
    
    # # loading customer balance 
    # ############################
    # # loan_obj=SLTLoan.objects.get(Sugan_id=id)
    # s=Customer_balance.objects.create(Sugan_id_id=id,current_balace=10000,Estimated_spend=10500)
    # s.shortage= s.Estimated_spend-s.current_balace
   
    # s.days_more=abs((date.today()).day-(s.Due_date).day)
    # print(s.days_more)
    # s.save()
    return HttpResponseRedirect(reverse('home'))


