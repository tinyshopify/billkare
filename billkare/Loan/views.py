from ast import Str
from json import dump, dumps
import pandas as pd

from datetime import date, datetime,timedelta
#Chart import libary
import base64
from io import BytesIO
from matplotlib import pyplot

import plaidlink
from plaidlink.models import plaidUser
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import customerLoanForm
from .models import PaymentInfo, customer_loan_decision_attrs, customer_loan_decision_attrs_history, customer_loan_history, customerLoan,PaymentSummary,PaymentSummaryHistory,customer_loan_decision_attrs_active
from User_Account import function
from .loanfunctions import calculate_days, put_customerLoan, get_total_avail_currrent_balance, is_paid
from membership.models import Subscription,CatcheSubscriptionlookup
from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required

dt=datetime.utcnow()


def Loan_page(request):
    id=function.get_user(request.user.email)
    context ={}
    obj = get_object_or_404(customer_loan_decision_attrs,id = id)
    # pass the object as instance in form
    form = customerLoanForm(request.POST or None, instance = obj)

    if form.is_valid():
        form.save()
        # return HttpResponseRedirect("/"+id)
        return HttpResponseRedirect(reverse('home'))
 
    # add form dictionary to context
    context["form"] = form
    return render(request,"Loan_page.html",context)

def dash_board(request):
    id=function.get_user(request.user.email)
    context = {}
    labels = []
    data = []
   
    ctx = customer_loan_decision_attrs.objects.get(catche_id_id = id)
    loan= customerLoan.objects.order_by('Loan_Type','PaymentDue_amount').filter(catche_id_id=id)
   
    for i in loan:
         labels.append(i.Loan_Type)
         data.append(i.PaymentDue_amount)
    print("labels",labels)
    print("data:",data)
    acc_labels = ['Balance','Estimated Balance','Shortage amount']
    acc_data = [ctx.balance,ctx.estimated_balance,ctx.shortage_bill_amount]
    
    context = {
        'labels': labels,
        'data': data,
        'nbar': 'home',
        'acc_labels':acc_labels,
        'acc_data':acc_data,

    }
    return render(request,"dashboard.html",context)
   
def loan_payment(request):
    id=function.get_user(request.user.email)
    # get_customerLoan(id)
    context ={}
    context["data"] = customerLoan.objects.filter(catche_id_id=id)
    obj= Subscription.objects.get(catche_id_id=id)
    sub=CatcheSubscriptionlookup.objects.get(Subscription_Type=obj.SubscriptionType_id)
    context["sub"]=sub
    return render(request,"loan_payment.html",context)

def Eligible_for_fund_cont1(request):
       return render(request,"Eligible_for_fund_cont1.html")

def transaction_details(request):
    id=function.get_user(request.user.email)
    context ={}
    messages=False

    total_avail_balance,total_current_balance=get_total_avail_currrent_balance(id)
    data = customer_loan_decision_attrs.objects.get(catche_id_id = id)
    if customerLoan.objects.filter(catche_id_id=id).exists():
         ctx = customerLoan.objects.filter(catche_id_id=id)
    else:
        ctx=None
        messages=True
    
    context = {"avail_balance":total_avail_balance,"current_balance":total_current_balance,"data1":ctx,"data":data,'messages':messages}
    context['nbar']='payments'
    return render(request,"transaction_details.html",context)

def update_shortage(request):
    print(request.method)
    id=function.get_user(request.user.email)
    total_avail_balance,total_current_balance=get_total_avail_currrent_balance(id)
    if request.method == 'POST':
        shortage=request.POST.get('shortage')
        print("Shortage",shortage)
        txtestimatedspend=request.POST.get('txtestimatedspend')
        id=function.get_user(request.user.email)
       
        # try:
        s=function.get_customer_loan_decision_attrs(id)
        s.loan_eligiblity_flag="yes"
        s.balance=total_current_balance
        s.estimated_balance= float(txtestimatedspend)
        s.shortage_bill_amount=shortage
        s.save()
        
        # except customer_loan_decision_attrs.DoesNotExist:
        #     customer_loan_decision_attrs.objects.create(catche_id_id=id,
        #     balance=total_current_balance,
        #     loan_eligiblity_flag="yes",
        #     estimated_balance= float(txtestimatedspend),
        #     shortage_bill_amount=shortage,)
        
        return render(request,"transaction_details.html")
    return render(request,"transaction_details.html")

def update_loan(request):
     print("updateloan")
     id=function.get_user(request.user.email)
     
     ctx = customerLoan.objects.filter(catche_id_id=id)
     print(ctx)
     if request.method == 'POST':
        user_due_amt=request.POST.getlist('user_due_amt1[]')
        user_due_date=request.POST.getlist('user_due_date1[]')
        
        days_more= request.POST.getlist('days_more1[]')
        print(user_due_amt,user_due_date,days_more)
        # dec_obj = customer_loan_decision_attrs.objects.get(catche_id_id = id)
        # dec_obj.Upload_statement=user_loan_stmt.getvalue()
        # dec_obj.save()
        x=0
        for i in ctx:
             i.PaymentDue_amount=user_due_amt[x]
            
             i.Due_date=user_due_date[x]
             i. days_more=days_more[x]
             i.creUser="live_user"
             i.InsUpdFlag ='U'
            #  print("x:",x)
            #  print(user_due_amt[x], user_due_date[x],days_more[x])
             i.save()
             x=x+1
        for s in ctx:
             customer_loan_history.objects.create(catche_id_id=id,
                                    Loan_Type=s.Loan_Type,
                                    PaymentDue_amount=s.PaymentDue_amount,
                                    Due_date=s.Due_date,days_more=s.days_more,
                                    creUser="live_user",InsUpdFlag ='U',)
       
        return render(request,"transaction_details.html")
     return render(request,"transaction_details.html")
def account_summary(request):
    id=function.get_user(request.user.email)
    context={}
    print("is paid",is_paid(id))
    total_avail_balance,total_current_balance=get_total_avail_currrent_balance(id)
    context = {"avail_balance":total_avail_balance,"current_balance":total_current_balance,'paid':is_paid(id)}
    # context["paysum"]=paysum
    context['nbar']='home'
    return render(request,"account_summarypage.html",context) 
    


def connect_bank(request):
    print("connect to bank")
    # id=function.get_user(request.user.email)
    return render(request,"connect_bank.html")

def Payment_summary(request):
    print("Payment_summary")
    id=function.get_user(request.user.email)
    if request.method == 'POST':
        bill1=request.POST.get('bill1')
        due=request.POST.get('due')
        fund_catche=request.POST.get('fund_catche')
        Plan_pay=request.POST.get('Plan_pay')
        fund_you=request.POST.get('fund_you')
        # print(bill1,fund_catche,Plan_pay,fund_you)
        loanobj=customerLoan.objects.get(Loan_Type=bill1,catche_id_id=id)
        print("next due date:",datetime.strptime(loanobj.Due_date,'%Y-%m-%d')+timedelta(days=30))
        next_due_date=(datetime.strptime(loanobj.Due_date,'%Y-%m-%d')+timedelta(days=30)).date()
        try:
          obj=PaymentSummary.objects.get(catche_id_id=id)
        #   messages.info(request,"Your Payment already proccessed")
          obj.Loan_Type=loanobj.Loan_Type
          obj.next_Duedate=next_due_date
          obj.PaymentDue_amount=loanobj.PaymentDue_amount
          obj.Planned_payment= Plan_pay
          obj.user_payment= fund_you
          obj.catche_fund=fund_catche
          obj.fund_return_amount=float(fund_catche)
          obj.creUser="live_user"
          obj.InsUpdFlag ='I'
          obj. is_paid='N'
        #   obj.days_more=abs(date.today()-next_due_date).days,
          obj.save()
          return redirect("view_Payment_summary")
        except PaymentSummary.DoesNotExist:
          print("object not created")
          PaymentSummary.objects.update_or_create(catche_id_id=id,
                                Loan_Type=loanobj.Loan_Type,
                                next_Duedate=next_due_date,
                                PaymentDue_amount=loanobj.PaymentDue_amount,
                                Planned_payment= Plan_pay,
                                user_payment= fund_you,catche_fund=fund_catche,
                                fund_return_amount=float(fund_catche),
                                creUser="live_user",
                                InsUpdFlag ='I',is_paid='N')
        #   s=PaymentSummary.objects.get(catche_id_id=id)
         
        #   print(type(s.next_Duedate))
        #   s.days_more=abs(date.today()-s.next_due_date).days
          
        #   s.save()
        return redirect("/")
    return redirect("/")

def view_Payment_summary(request): 
    id=function.get_user(request.user.email)
    print(id)
    registered=False
    obj=function.get_payment_summary(id)
    if obj==None:
        registered=True
        return render(request,"Payment_summary.html",{'registered':registered,'nbar':'pay_summary'})
    context ={}
    context["data"] =obj
    context['nbar']='pay_summary'
    return render(request,"Payment_summary.html",context)
def cancelPayment(request):
     id=function.get_user(request.user.email)
     obj=function.get_payment_summary(id)
     obj.delete()
     return redirect('transaction_details')

def PaymentHistory(request):
    id=function.get_user(request.user.email)
    obj=function.get_payment_summary(id)
    if obj.is_paid== 'Y':
        messages.error="Dear user your payment aleady done"
        return redirect('account_summary')
    obj.is_paid="Y"
    obj.save()
    PaymentSummaryHistory.objects.update_or_create(catche_id_id=id,
                                Loan_Type=obj.Loan_Type,
                                PaymentDue_amount=obj.PaymentDue_amount,
                                Planned_payment= obj.Planned_payment,
                                user_payment= obj.user_payment,
                                catche_fund=obj.catche_fund,
                                fund_return_amount=obj.fund_return_amount,
                                is_paid="Y",
                                creUser="live_user",
                                InsUpdFlag ='I',
                                CreatedTs  =dt,
                                UpdateTs=dt,)
    return redirect('account_summary')
def paymentInfo(request):
    id=function.get_user(request.user.email)
    obj=function.get_payment_summary(id)
    try:
        payinfo=PaymentInfo.objects.get(catche_id_id=id)
        return redirect('view_Payment_summary')
    except PaymentInfo.DoesNotExist:
         print(request.method)
         if request.method == 'POST':
            accno=request.POST.get('accno')
            company=request.POST.get('company')
            street=request.POST.get('street')
            zip=request.POST.get('zip')
            state=request.POST.get('state')
            country=request.POST.get('country')
            # print("accno:",accno)
            # print(request.POST.get('street'))
            # print(request.POST.get('company'),request.POST.get('zip'),request.POST.get('state'),request.POST.get('country'))
            # print(request.POST.get('check_box1'))
            deliveryoption=request.POST.get('check_box1')
            PaymentInfo.objects.update_or_create(
                                catche_id_id=id,
                                loan_type=obj.Loan_Type,
                                account_number=accno,
                                company=company,
                                firstname=request.user.first_name,
                                lastname=request.user.last_name,
                                street=street,
                                zip=zip,
                                state=state,
                                country=country,
                                delivery_option= deliveryoption,
                                creUser="live_user",
                                InsUpdFlag ='I',
                                CreatedTs  =dt,
                                UpdateTs=dt,)
            return redirect('view_Payment_summary')
    return render(request,"paymentinfo.html",{'data':obj})