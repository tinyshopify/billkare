
from django.db import models
import datetime
import uuid 
from django.core.validators import FileExtensionValidator
from django.utils.timezone import now
from User_Account.models import User
from plaidlink.models import plaidUser

def get_deadline():
    return datetime.date.today()+ datetime.timedelta(days=30)
def get_duedate():
    
    duedate= datetime.date.today()+ datetime.timedelta(days=20)
    return duedate.strftime('%Y-%m-%d')


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
    mortgage_due_date=models.CharField(default=get_duedate(),null=True,blank=True,max_length=50,)
    auto_loan_amount=models.FloatField(default=0)
    auto_due_date=models.CharField(default=get_duedate(),null=True,db_index=True,blank=True,max_length=50)
    creditcard_min_paydue_amount=models.FloatField(default=0)
    creditcard_statment_balance_amount=models.FloatField(default=0)
    creditcard_due_date=models.CharField(default=get_duedate(),null=True,db_index=True,blank=True,max_length=50,)
    loan_eligiblity_flag=models.CharField(max_length=50,default=None,db_index=True,blank=True)
    max_loan_amount_from_catche=models.FloatField(default=0)
    min_loan_amount_from_catche=models.FloatField(default=0)
    estimated_balance=models.FloatField(default=0.0)
    shortage_bill_amount=models.FloatField(default=0.0)
    paycheck_date=models.CharField(default=get_duedate(),max_length=50,null=True,db_index=True,blank=True)
    catche_risk_score_0_100=models.IntegerField(default=0)
    customer_entered_bill_amount=models.FloatField(default=0)
    catche_bill_due_date=models.CharField(default=get_deadline(),max_length=50,null=True,db_index=True,blank=True) 
    Upload_statement= models.FileField(upload_to ='uploads/loanstatements/%Y/%m/%d',null=True,validators=[FileExtensionValidator(['pdf'])]) 

class customerLoan(TimeStampModel):
     catche_id= models.ForeignKey(User,on_delete=models.CASCADE,default=uuid.uuid4 )
     Loan_Type=models.CharField(max_length=50,default=0)
     PaymentDue_amount=models.FloatField(("Minimum Due amount"),default="$")
     Due_date = models.CharField(("Due Date"),blank=True,max_length=50,null=True,default=get_duedate())
     days_more=models.IntegerField(default=0)
     

class customer_loan_history(TimeStampModel):
     EventID=models.UUIDField(primary_key=True,editable=False,unique=True,default=uuid.uuid4 )
     catche_id= models.ForeignKey(User,on_delete=models.CASCADE,default=uuid.uuid4 )
     Loan_Type=models.CharField(max_length=50,default=0)
     PaymentDue_amount=models.FloatField(("Minimum Due amount"),default="$")
     Due_date = models.CharField(("Due Date"),blank=True,max_length=50,null=True,default=get_duedate())
     days_more=models.IntegerField(default=0)
    

class PaymentSummary(TimeStampModel):
    catche_id= models.ForeignKey(User,on_delete=models.CASCADE,default=uuid.uuid4)
    Loan_Type=models.CharField(max_length=50,default=0)
    next_Duedate = models.CharField(("Due Date"),blank=True,max_length=50,null=True)
    PaymentDue_amount=models.FloatField(("Minimum Due amount"))
    Planned_payment=models.FloatField(("Your Planned Payment"))
    user_payment=models.FloatField(("Your Payment"))
    catche_fund=models.FloatField(("Fund From Catche"),default=0)
    fund_return_date=models.CharField(("Fund return Date"),max_length=50,default=str((datetime.date.today()+datetime.timedelta(days=10))))
    fund_return_amount =models.FloatField(default=0)
    current_paydate=models.CharField(default=now,max_length=50)
    is_paid=models.CharField(max_length=10,blank=True,null=True)
    days_more=models.IntegerField(default=0)

class PaymentSummaryHistory(TimeStampModel):
    catche_id= models.ForeignKey(User,on_delete=models.CASCADE,default=uuid.uuid4)
    Loan_Type=models.CharField(max_length=50,default=0)
    PaymentDue_amount=models.FloatField(("Minimum Due amount"))
    next_Duedate = models.CharField(("Due Date"),max_length=50,default=get_deadline(),blank=True,null=True)
    Planned_payment=models.FloatField(("Your Planned Payment"))
    user_payment=models.FloatField(("Your Payment"))
    catche_fund=models.FloatField(("Fund From Catche"),default=0)
    fund_return_date=models.CharField(("Fund return Date"),max_length=50,default=(get_deadline()+datetime.timedelta(days=10)))
    fund_return_amount =models.FloatField(default=0)
    current_paydate=models.CharField(default=now,max_length=50,)
    is_paid=models.CharField(max_length=10,blank=True,null=True)

class PaymentInfo(TimeStampModel):
    catche_id= models.ForeignKey(User,on_delete=models.CASCADE,default=uuid.uuid4)
    loan_type=models.CharField(max_length=50,default=0)
    account_number=models.CharField(max_length=50,default=0)
    company=models.CharField(max_length=50,default=0)
    firstname=models.CharField(max_length=50,default=0)
    lastname=models.CharField(max_length=50,default=0)
    street=models.CharField(max_length=50,default=0)
    zip=models.CharField(max_length=50,default=0)
    state=models.CharField(max_length=50,default=0)
    country=models.CharField(max_length=50,default=0)
    delivery_option=models.CharField(max_length=50,default=0)

class customer_loan_decision_attrs_active(TimeStampModel):  
    
    EventID=models.UUIDField(primary_key=True,editable=False,unique=True,default=uuid.uuid4 )
    catche_id= models.ForeignKey(User,on_delete=models.CASCADE,default=uuid.uuid4)
    plaid_id =models.ForeignKey(plaidUser,on_delete=models.CASCADE,default=uuid.uuid4)
    access_token=models.CharField(max_length=50,blank=True,null=True)
    account_id=models.CharField(max_length=50,blank=True,null=True)
    available_balance=models.FloatField(max_length=50,blank=True)
    current_balance=models.FloatField(max_length=50,blank=True)
    iso_currency_code=models.CharField(max_length=50,blank=True,null=True)
    limit=models.CharField(max_length=50,blank=True,null=True)
    unofficial_currency_code=models.CharField(max_length=50,blank=True,null=True)
    mask=models.CharField(max_length=50,blank=True,null=True)
    name=models.CharField(max_length=50,blank=True,null=True)
    official_name=models.CharField(max_length=50,blank=True,null=True)
    subtype=models.CharField(max_length=50,blank=True,null=True)
    type=models.CharField(max_length=50,blank=True,null=True)
   

class customer_loan_decision_attrs_history(TimeStampModel):  
    
    EventID=models.UUIDField(primary_key=True,editable=False,unique=True,default=uuid.uuid4 )
    catche_id= models.ForeignKey(User,on_delete=models.CASCADE,default=uuid.uuid4)
    plaid_id =models.ForeignKey(plaidUser,on_delete=models.CASCADE,default=uuid.uuid4)
    access_token=models.CharField(max_length=50,blank=True,null=True)
    account_id=models.CharField(max_length=50,blank=True,null=True)
    available_balance=models.FloatField(max_length=50,blank=True)
    current_balance=models.FloatField(max_length=50,blank=True)
    iso_currency_code=models.CharField(max_length=50,blank=True,null=True)
    limit=models.CharField(max_length=50,blank=True,null=True)
    unofficial_currency_code=models.CharField(max_length=50,blank=True,null=True)
    mask=models.CharField(max_length=50,blank=True,null=True)
    name=models.CharField(max_length=50,blank=True,null=True)
    official_name=models.CharField(max_length=50,blank=True,null=True)
    subtype=models.CharField(max_length=50,blank=True,null=True)
    type=models.CharField(max_length=50,blank=True,null=True)

