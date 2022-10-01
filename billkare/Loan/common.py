from .models import PaymentSummaryHistory, customer_loan_decision_attrs,customerLoan,PaymentSummary
from datetime import date


def  get_customerLoan(id):
 delloan=customerLoan.objects.filter(catche_id_id=id)
 delloan.delete()
 loanobj=customerLoan()
 print(id)
 customerLoanAttr=customer_loan_decision_attrs.objects.get(catche_id_id=id)
 print(customerLoanAttr.mortgage_due_amount)
 if customerLoanAttr.mortgage_due_amount== 0 and customerLoanAttr.mortgage_due_date==None and customerLoanAttr.auto_loan_amount==0 and customerLoanAttr.auto_due_date==None and customerLoanAttr.creditcard_min_paydue_amount==0 and customerLoanAttr.creditcard_statment_balance_amount==0 and customerLoanAttr.creditcard_due_date==None :
    return None
 print("Check loan details")
 print(customerLoanAttr.mortgage_due_amount)
 if float(customerLoanAttr.mortgage_due_amount) > 0:
    customerLoan.objects.create(catche_id_id=id,
    Loan_Type="Mortgage",
    PaymentDue_amount=customerLoanAttr.mortgage_due_amount,
    Due_date=customerLoanAttr.mortgage_due_date,
    days_more=calculate_days(customerLoanAttr.mortgage_due_date))
    
    print("mortgage")
 print(customerLoanAttr.auto_loan_amount>0)
 if float(customerLoanAttr.auto_loan_amount) >0:
    customerLoan.objects.create(catche_id_id=id,
    Loan_Type="Auto",
    PaymentDue_amount=customerLoanAttr.auto_loan_amount
                     ,Due_date=customerLoanAttr.auto_due_date,
                     days_more= calculate_days(customerLoanAttr.auto_due_date))
    print("Auto")
 if  customerLoanAttr.creditcard_min_paydue_amount >0:
    customerLoan.objects.create(catche_id_id=id,
    Loan_Type="Creditcard"
    ,PaymentDue_amount=customerLoanAttr.creditcard_min_paydue_amount
    ,Due_date=customerLoanAttr.creditcard_due_date,
    days_more=calculate_days(customerLoanAttr.creditcard_due_date))
    print("Credit")

def calculate_days(duedate):
  
   days=abs((date.today()).day-(duedate).day)
   return days

def is_paid(id):
    try:
        obj=PaymentSummary.objects.get(catche_id_id=id) 
    except PaymentSummary.DoesNotExist: 
        return False
    return True
