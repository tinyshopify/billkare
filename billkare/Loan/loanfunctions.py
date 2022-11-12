from .models import PaymentSummaryHistory, customer_loan_decision_attrs, customer_loan_history,customerLoan,PaymentSummary,customer_loan_decision_attrs_active
from datetime import date, datetime, timedelta
from django.db.models import Q

def  put_customerLoan(id):

 if customerLoan.objects.filter(catche_id_id=id).exists():
    # delloan=customerLoan.objects.filter(catche_id_id=id)
    # delloan.delete()
    days=customerLoan.objects.filter(catche_id_id=id)
    for i in days:
      i.days_more=calculate_days(i.Due_date)
      i.save()
    return

 try:
            customer_loans=customer_loan_decision_attrs_active.objects.filter(Q(type='loan') | Q(type='credit') ).filter(catche_id_id = id)
        
            for i in customer_loans:
                print(i.subtype)
                s=customerLoan.objects.create(catche_id_id=id,
                                    Loan_Type=i.subtype.replace(" ", ""),
                                    PaymentDue_amount=i.current_balance,creUser="live_user",InsUpdFlag ='I',)
                s.days_more=calculate_days(s.Due_date)
                s.save()
                customer_loan_history.objects.create(catche_id_id=id,
                                    Loan_Type=s.Loan_Type,
                                    PaymentDue_amount=s.PaymentDue_amount,Due_date=s.Due_date,days_more=s.days_more,creUser="live_user",InsUpdFlag ='I')
                
 except customer_loan_decision_attrs_active.DoesNotExist:
        return None
 
def calculate_days(duedate):
   print( "Due date:",duedate)
   duedate=(datetime.strptime((duedate.replace(" ", "")),'%Y-%m-%d')).date()
   print("duedate:",duedate)
   # print(date.today())
   # days=abs((date.today()).day-(duedate).day)
   days=abs(date.today()-(duedate)).days
   print("days_more",days)
   return days

def is_paid(id):
    try:
        obj=PaymentSummary.objects.get(catche_id_id=id) 
        if obj.is_paid=='Y':
         return True
        else:
         obj.delete()
         return False
    except PaymentSummary.DoesNotExist: 
        return False
def get_total_avail_currrent_balance(id):
    
    total_avail_balance=0
    total_current_balance=0
    avail_current_balances= customer_loan_decision_attrs_active.objects.values_list("available_balance","current_balance").filter(catche_id_id = id).filter(type='depository')
 
    for ele in range(0, len(avail_current_balances)):
        for j in range(0,1):
            total_avail_balance = total_avail_balance + avail_current_balances[ele][j]
            total_current_balance =total_current_balance + avail_current_balances[ele][j+1]
    return total_avail_balance,total_current_balance
