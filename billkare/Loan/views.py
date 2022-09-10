
from datetime import datetime,timedelta
from datetime import date

from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import SLTLoanForm,SlT_Payment_summaryForm
from .models import SLTLoan,SlT_summary,SlT_Payment_summary
from User_Account import function
from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required



def Loan_page(request):
    id=function.get_user(request.user.email)
    context ={}
    obj = get_object_or_404(SLTLoan,id = id)
    # pass the object as instance in form
    form = SLTLoanForm(request.POST or None, instance = obj)

    if form.is_valid():
        form.save()
        # return HttpResponseRedirect("/"+id)
        return HttpResponseRedirect(reverse('home'))
 
    # add form dictionary to context
    context["form"] = form
    return render(request,"Loan_page.html",context)

def Eligible_for_fund (request,limit):
    id=function.get_user(request.user.email)
    context ={}
    context["data"] = SLTLoan.objects.filter(SLT_id_id=id)
    context['limit']=limit
    print(limit)
    return render(request,"Eligible_for_fund.html",context)

def Eligible_for_fund_cont1(request):
       return render(request,"Eligible_for_fund_cont1.html")

def transaction_details(request):
    id=function.get_user(request.user.email)
    context ={}
    s=function.get_summaryobject(id)
    print(s.Due_date)
    days=abs((date.today()).day-(s.Due_date).day)
    s.days_more= days
    s.save()
    context["data"] =s
    return render(request,"transaction_details.html",context)

def update_shortage(request):
    print(request.method)
    if request.method == 'POST':
        shortage=request.POST.get('shortage')
        extra_amount=request.POST.get('extra_amount')
        id=function.get_user(request.user.email)
        s=function.get_summaryobject(id)
        s.Estimated_spend=s.Estimated_spend+ float(extra_amount)
        s.shortage=shortage
        s.save()
        return render(request,"transaction_details.html")
    return render(request,"transaction_details.html")
    

def connect_bank(request):
    print("connect to bank")
    id=function.get_user(request.user.email)
    # loan_obj=SLTLoan.objects.get(SLT_id=sltauth.sourcelantics_id)
    s=SlT_summary.objects.create(SLT_id_id=id,current_balace=10000,Estimated_spend=10500)
    s.shortage=500
    # print(s.Due_date)
    # print(abs((date.today()).day-(s.Due_date).day))
    s.days_more=abs((date.today()).day-(s.Due_date).day)
    print(s.days_more)
    s.save()
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
        # loanobj=SLTLoan.objects.filter(SLT_id_id=id).filter(Loan_Type=bill1)
        # print(loanobj)
        # print(loanobj.PaymentDue_amount)
        obj=SlT_Payment_summary()
        obj.SLT_id_id=id
        obj.Loan_Type=bill1
        obj.PaymentDue_amount=due
        obj.Planned_payment= Plan_pay
        obj.user_payment= fund_you
        obj.cathe_fund=fund_catche
        obj.fund_return_amount=float(fund_catche) + 50.0
        obj.save()
        return redirect("/")
    return redirect("/")
    
def view_Payment_summary(request):
    id=function.get_user(request.user.email)
    print(id)
    context ={}
    context["data"] =SlT_Payment_summary.objects.get(SLT_id_id=id)
    return render(request,"Payment_summary.html",context)
