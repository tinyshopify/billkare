
from django.db import models
import datetime
import uuid 

from django.utils.timezone import now
from User_Account.models import User

def get_deadline():
    return datetime.date.today()+ datetime.timedelta(days=30)
def get_duedate():
     return datetime.date.today()+ datetime.timedelta(days=20)


class TimeStampModel(models.Model):
    isActive        = models.BooleanField(default=True,db_index=True)
    creUser         =models.CharField(max_length=50,db_index=True,blank=True,null=True)
    CreatedTs       =models.DateTimeField(null=True,db_index=True)
    UpdateTs        =models.DateTimeField(null=True,db_index=True)
    creDate         =models.DateTimeField(auto_now_add=True,null=True,db_index=True)
    InsUpdFlag      =models.CharField(max_length=50,null=True,db_index=True)
   

    class Meta:
        abstract = True
        
class customer_loan_decision_attrs(TimeStampModel):
    catche_id= models.ForeignKey(User,on_delete=models.CASCADE,default=uuid.uuid4)
    balance  =models.FloatField(default=0)
    loanType=models.CharField(max_length=50,default=None,null=True,blank=True,db_index=True)
    mortgage_due_amount=models.FloatField(default=0)
    mortgage_due_date=models.DateField(default=get_duedate(),null=True,blank=True)
    auto_loan_amount=models.FloatField(default=0)
    auto_due_date=models.DateField(default=get_duedate(),null=True,db_index=True,blank=True)
    creditcard_min_paydue_amount=models.FloatField(default=0)
    creditcard_statment_balance_amount=models.FloatField(default=0)
    creditcard_due_date=models.DateField(default=get_duedate(),null=True,db_index=True,blank=True)
    loan_eligiblity_flag=models.CharField(max_length=50,default=None,db_index=True,blank=True)
    max_loan_amount_from_catche=models.FloatField(default=0)
    min_loan_amount_from_catche=models.FloatField(default=0)
    estimated_balance=models.FloatField(default=0)
    shortage_bill_amount=models.FloatField(default=0)
    paycheck_date=models.DateField(default=get_duedate(),null=True,db_index=True,blank=True)
    catche_risk_score_0_100=models.IntegerField(default=0)
    customer_entered_bill_amount=models.FloatField(default=0)
    catche_bill_due_date=models.DateField(default=get_deadline(),null=True,db_index=True,blank=True) 


class customerLoan(models.Model):
     catche_id= models.ForeignKey(User,on_delete=models.CASCADE,default=uuid.uuid4 )
     Loan_Type=models.CharField(max_length=50,default=0)
     PaymentDue_amount=models.FloatField(("Minimum Due amount"),default="$")
     Due_date = models.DateField(("Due Date"),default=get_deadline())
     days_more=models.IntegerField(default=0)

class PaymentSummary(TimeStampModel):
    catche_id= models.ForeignKey(User,on_delete=models.CASCADE,default=uuid.uuid4)
    Loan_Type=models.CharField(max_length=50,default=0)
    Due_date = models.DateField(("Due Date"),default=get_deadline(),blank=True,null=True)
    PaymentDue_amount=models.FloatField(("Minimum Due amount"))
    Planned_payment=models.FloatField(("Your Planned Payment"))
    user_payment=models.FloatField(("Your Payment"))
    catche_fund=models.FloatField(("Fund From Catche"),default=0)
    fund_return_date=models.DateField(("Fund return Date"),default=(get_deadline()+datetime.timedelta(days=10)))
    fund_return_amount =models.FloatField(default=0)
    current_paydate=models.DateField(default=now)
    is_paid=models.CharField(max_length=10,blank=True,null=True)
    days_more=models.IntegerField(default=0)

class PaymentSummaryHistory(TimeStampModel):
    catche_id= models.ForeignKey(User,on_delete=models.CASCADE,default=uuid.uuid4)
    Loan_Type=models.CharField(max_length=50,default=0)
    PaymentDue_amount=models.FloatField(("Minimum Due amount"))
    Due_date = models.DateField(("Due Date"),default=get_deadline(),blank=True,null=True)
    Planned_payment=models.FloatField(("Your Planned Payment"))
    user_payment=models.FloatField(("Your Payment"))
    catche_fund=models.FloatField(("Fund From Catche"),default=0)
    fund_return_date=models.DateField(("Fund return Date"),default=(get_deadline()+datetime.timedelta(days=10)))
    fund_return_amount =models.FloatField(default=0)
    current_paydate=models.DateField(default=now)
    is_paid=models.CharField(max_length=10,blank=True,null=True)

class PaymentInfo(TimeStampModel):
    catche_id= models.ForeignKey(User,on_delete=models.CASCADE,default=uuid.uuid4)
    loan_type=models.CharField(max_length=50,default=0)
    account_number=models.CharField(max_length=50,default=0)
    Due_date=models.DateField(("Due Date"))
    Payment_address=models.CharField(max_length=50,default=0)
    delivery_option=models.CharField(max_length=50,default=0)
