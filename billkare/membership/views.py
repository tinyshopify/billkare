
from django.shortcuts import render,redirect
from User_Account import function
from Loan.models import SLTLoan,SlT_summary
from .models import SLT_membership


def no_membership(request):
    id=function.get_user(request.user.email)
    context={}
    context["data"] =function.get_summaryobject(id)
    return render(request,'no_membership.html',context)

def add_membership(request):
    id=function.get_user(request.user.email)
    s=function.get_summaryobject(id)
    if request.method == 'POST':
        membership=request.POST.get('check_box1')
        print(membership)
        # print(s.shortage)
        # print(membership == ['Basic'])
        limit=800
        if s.shortage > 200 and membership == 'Basic':
            print("no eligible")
            return render(request,'need_upgrade.html',{'data':s.shortage})
        SLT_membership.objects.update_or_create( SLT_id_id=id,membership=membership)
        if membership == 'Basic':limit=200
        return redirect('Eligible_for_fund',limit)
    
    return render(request,'no_membership.html')

def check_membership(request):
    id=function.get_user(request.user.email)
    s=function.get_summaryobject(id)
    membership=function.get_membership(id)
    # print(membership)
    print(membership == 'Basic')
    if membership == None:
      print("currently no membership")
      return redirect('no_membership')
    if membership =='Basic' and s.shortage > 200:
            print("no eligible")
            return render(request,'need_upgrade.html',{'data':s.shortage})
    if membership =='Basic':
        print(membership)
        limit=200
    else: 
        limit=800
    print(limit)
    return redirect('Eligible_for_fund',limit)




    


