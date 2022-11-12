import datetime

from django.db import models
import uuid
from django.utils.timezone import now
from User_Account.models import User



def get_deadline():
    return datetime.date.today()+ datetime.timedelta(days=30)

class TimeStampModel(models.Model):
    isActive        = models.BooleanField(default=True,db_index=True)
    creUser         =models.CharField(max_length=50,default=None,db_index=True)
    CreatedTs       =models.DateTimeField(null=True,db_index=True)
    UpdateTs        =models.DateTimeField(null=True,db_index=True)
    creDate         =models.DateTimeField(auto_now_add=True,null=True,db_index=True)
    InsUpdFlag      =models.CharField(max_length=50,null=True,db_index=True)
   

    class Meta:
        abstract = True

class CatcheSubscriptionlookup(TimeStampModel):
  
    Subscription_Type=models.CharField(primary_key=True,max_length=50,blank=True,unique=True)
    SubscriptionName=models.CharField(max_length=50,blank=True)
    SubscriptionAmount=models.FloatField(default=0)
    Subscription_limit=models.FloatField(default=0)
    Description=models.CharField(max_length=50,blank=True)

class Subscription(TimeStampModel):
    SubscriptionID=models.UUIDField(primary_key=True,editable=False,unique=True,default=uuid.uuid4)
    catche_id       = models.ForeignKey(User,on_delete=models.CASCADE,default=uuid.uuid4 )
    SubscriptionType=models.ForeignKey(CatcheSubscriptionlookup,on_delete=models.CASCADE)
    SubscriptionStartDate=models.DateTimeField(auto_now_add=True,db_index=True)
    SubscriptionEndDate=models.DateTimeField(default=get_deadline(),db_index=True)

class SubscriptionHistory(TimeStampModel):
    EventID=models.UUIDField(primary_key=True,editable=False,unique=True,default=uuid.uuid4)
    SubscriptionID=models.ForeignKey(Subscription,on_delete=models.CASCADE,default=uuid.uuid4)
    catche_id       = models.ForeignKey(User,on_delete=models.CASCADE,default=uuid.uuid4 )
    SubscriptionType=models.ForeignKey(CatcheSubscriptionlookup,on_delete=models.CASCADE)
    Subscription_Reason=models.CharField(max_length=50,blank=True)
    SubscriptionStartDate=models.DateTimeField(auto_now_add=True,db_index=True)
    SubscriptionEndDate=models.CharField(default=get_deadline(),db_index=True,max_length=50)
    Refund_Amount=models.FloatField(default=0)




