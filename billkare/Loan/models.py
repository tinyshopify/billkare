
from django.db import models
import datetime
import uuid
from User_Account.models import SLTAuth

def get_deadline():
    return datetime.date.today()+ datetime.timedelta(days=20)

class SLTLoan(models.Model):
     SLT_id= models.ForeignKey(SLTAuth,on_delete=models.CASCADE,default=uuid.uuid4 )
     acount_number=models.CharField(max_length=50,blank=True)
     Address=models.CharField(max_length=50,blank=True)
     company_name=models.CharField(max_length=50,blank=True)
     Loan_Type=models.CharField(max_length=50,default=0)
     PaymentDue_amount=models.FloatField(("Minimum Due amount"),default="$")
     Due_date = models.DateField(("Due Date"),default=get_deadline())
     
     def __str__(self):
        return '%s %s %f'%(self.id,self.Loan_Type,self.PaymentDue_amount)


class SlT_summary(models.Model):
    SLT_id= models.ForeignKey(SLTAuth,on_delete=models.CASCADE,default=uuid.uuid4 )
    # Due_date=models.ForeignKey(SLTLoan,on_delete=models.CASCADE,default=1) 
    Due_date = models.DateField(("Due Date"),default=get_deadline()) 
    current_balace=models.FloatField(("Minimum Due amount"),default="$")
    Estimated_spend=models.FloatField(("Minimum Due amount"),default="$")
    shortage=models.FloatField(default=0)
    days_more=models.IntegerField(default=0)
    
    def __str__(self):
        return self.id

class SlT_Payment_summary(models.Model):
    SLT_id= models.ForeignKey(SLTAuth,on_delete=models.CASCADE,default=uuid.uuid4)
    Loan_Type=models.CharField(max_length=50,default=0)
    PaymentDue_amount=models.FloatField(("Minimum Due amount"))
    Planned_payment=models.FloatField(("Your Planned Payment"))
    user_payment=models.FloatField(("Your Payment"))
    cathe_fund=models.FloatField(("Fund From Cathe"))
    fund_return_date=models.DateField(("Fund return Date"),default=(get_deadline()+datetime.timedelta(days=10)))
    fund_return_amount =models.FloatField(default=0)

   