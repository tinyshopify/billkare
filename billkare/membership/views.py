
from django.shortcuts import render,redirect
from User_Account import function
from Loan.models import customer_loan_decision_attrs

from . import membership_function
from .models import Subscription,CatcheSubscriptionlookup

def subscription_details(request):
     return render(request,'subscription_details.html',{'nbar': 'sub'})
def no_membership(request):
    id=function.get_user(request.user.email)
    context={}
    context["data"] =function.get_customer_loan_decision_attrs(id)
    return render(request,'no_membership.html',context)
def update_membership(request):
    id=function.get_user(request.user.email)
    s=function.get_customer_loan_decision_attrs(id)
    print("add member")
    if request.method == 'POST':
        print("postmethod")
        membership=request.POST.get('check_box1')
        print(membership)
        obj=CatcheSubscriptionlookup.objects.get(SubscriptionName=membership)
        print(obj.SubscriptionAmount)
        membership_function.addmembership(id,obj,request.user.first_name)
        return redirect('subscription')
    return redirect('subscription')

def add_membership(request):
    id=function.get_user(request.user.email)
    s=function.get_customer_loan_decision_attrs(id)
    print("add member")
    if request.method == 'POST':
        print("postmethod")
        membership=request.POST.get('check_box1')
        # procced=request.POST.get('check_box1')
        print(membership)
        obj=CatcheSubscriptionlookup.objects.get(SubscriptionName=membership)
        print(obj.SubscriptionAmount)
        if s.shortage_bill_amount > obj.SubscriptionAmount and membership == obj.SubscriptionName:
            print("no eligible")
            return render(request,'need_upgrade.html',{'data':s.shortage_bill_amount})
        membership_function.addmembership(id,obj,request.user.first_name)
        return redirect('loan_payment')
    return render(request,'no_membership.html')

def shortage_membership(request):
    id=function.get_user(request.user.email)
    print(id)
    s=function.get_customer_loan_decision_attrs(id)
    print("shortage")
    if request.method == 'POST':
        membership=request.POST.get('Procced')
        obj=CatcheSubscriptionlookup.objects.get(SubscriptionName=membership)
        membership_function.addmembership(id,obj,request.user.first_name)
        return redirect('loan_payment')
    print("form submited")
    return render(request,'need_upgrade.html',{'data':s.shortage_bill_amount})

def cancelmembership(request):
     id=function.get_user(request.user.email)
     membership_function.cancelmembership(id,request.user.first_name)
     return redirect('subscription')


def check_membership(request):
    id=function.get_user(request.user.email)
    s=function.get_customer_loan_decision_attrs(id)
    print("s.shortage_bill_amount",s.shortage_bill_amount)
   
    membership_id=membership_function.get_membership(id)
    print(" membership_id", membership_id)
    if membership_id == None:
      print("currently no membership")
      return redirect('transaction_details')
    obj=membership_function.get_base(membership_id)
    print("obj.SubscriptionAmount",obj.SubscriptionAmount)
    print( int(membership_id) == 2)
    if membership_id == "1" and s.shortage_bill_amount> obj.SubscriptionAmount:
            print("no eligible")
            return redirect('no_membership')
    if membership_id == "2" and s.shortage_bill_amount> obj.SubscriptionAmount:
            print("upgrde to basic to premium")
            return render(request,'need_upgrade.html',{'data':s.shortage_bill_amount})
    return redirect('loan_payment')

def subscription(request):
    id=function.get_user(request.user.email)
    s=function.get_customer_loan_decision_attrs(id)
    membership=membership_function.get_membership(id)
    print(membership)
    if membership == None: 
        membership='No'
    obj=membership_function.get_base(membership)
    return render(request,'subscription.html',{'membership':obj.SubscriptionName,'nbar': 'sub'})



    


