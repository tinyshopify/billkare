
import datetime
from datetime import date


from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import SLTLoanForm
from .models import PaymentInfo, customer_loan_decision_attrs, customerLoan,PaymentSummary,PaymentSummaryHistory
from User_Account import function
from .common import calculate_days, get_customerLoan, is_paid
from membership.models import Subscription,CatcheSubscriptionlookup
from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required

dt=datetime.datetime.utcnow()


def Loan_page(request):
    id=function.get_user(request.user.email)
    context ={}
    obj = get_object_or_404(customer_loan_decision_attrs,id = id)
    # pass the object as instance in form
    form = SLTLoanForm(request.POST or None, instance = obj)

    if form.is_valid():
        form.save()
        # return HttpResponseRedirect("/"+id)
        return HttpResponseRedirect(reverse('home'))
 
    # add form dictionary to context
    context["form"] = form
    return render(request,"Loan_page.html",context)

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
    context = {}
    ctx = customer_loan_decision_attrs.objects.get(catche_id = id)
    context["data1"] = customerLoan.objects.filter(catche_id_id=id)
    context["data"] = ctx
    context['nbar']='home'
    return render(request,"transaction_details.html",context)

def update_shortage(request):
    print(request.method)
    if request.method == 'POST':
        shortage=request.POST.get('shortage')
        extra_amount=request.POST.get('extra_amount')
        id=function.get_user(request.user.email)
        s=function.get_customer_loan_decision_attrs(id)
        s.estimated_balance=s.estimated_balance+ float(extra_amount)
        s.shortage_bill_amount=shortage
        s.save()
        return render(request,"transaction_details.html")
    return render(request,"transaction_details.html")
    
def billing_details(request):
    id=function.get_user(request.user.email)
    context={}
    ctx = customer_loan_decision_attrs.objects.get(catche_id_id = id)
    paysum=PaymentSummary.objects.get(catche_id_id = id)
    context["paid"] =True
    context["data"] = ctx
    context["paysum"]=paysum
    return render(request,"billing_details.html",context)

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
        print(bill1,fund_catche,Plan_pay,fund_you)
        loanobj=customerLoan.objects.get(Loan_Type=bill1,catche_id_id=id)
        print(loanobj)
        print(loanobj.PaymentDue_amount)
        try:
          obj=PaymentSummary.objects.get(catche_id_id=id)
        #   messages.info(request,"Your Payment already proccessed")
          return redirect("view_Payment_summary")
        except PaymentSummary.DoesNotExist:
          print("object not created")
          PaymentSummary.objects.update_or_create(catche_id_id=id,
                                Loan_Type=loanobj.Loan_Type,
                                PaymentDue_amount=loanobj.PaymentDue_amount,
                                Planned_payment= Plan_pay,
                                user_payment= fund_you,catche_fund=fund_catche,
                                fund_return_amount=float(fund_catche),
                                creUser="live_user",
                                InsUpdFlag ='I',is_paid='N')
          s=PaymentSummary.objects.get(catche_id_id=id,)
          s.days_more=calculate_days(s.Due_date)
          s.save()
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
        return redirect('billing_details')
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
                                InsUpdFlag ='U',
                                CreatedTs  =dt,
                                UpdateTs=dt,)
    return redirect('billing_details')
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
            address=request.POST.get('address')
            deliveryoption=request.POST.get('check_box1')
            PaymentInfo.objects.update_or_create(
                                catche_id_id=id,
                                loan_type=obj.Loan_Type,
                                account_number=accno,
                                Due_date=obj.Due_date,
                                Payment_address=address,
                                delivery_option= deliveryoption,
                                creUser="live_user",
                                InsUpdFlag ='I',
                                CreatedTs  =dt,
                                UpdateTs=dt,)
            return redirect('view_Payment_summary')
    return render(request,"paymentinfo.html",{'data':obj})