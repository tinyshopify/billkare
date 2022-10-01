from django.db import models
import uuid


from User_Account.models import User



class TimeStampModel(models.Model):
    isActive        = models.BooleanField(default=True,db_index=True)
    creUser         =models.CharField(max_length=50,default=None,db_index=True)
    CreatedTs       =models.DateTimeField(null=True,db_index=True)
    UpdateTs        =models.DateTimeField(null=True,db_index=True)
    creDate         =models.DateTimeField(auto_now_add=True,null=True,db_index=True)
    InsUpdFlag      =models.CharField(max_length=50,null=True,db_index=True)
   

    class Meta:
        abstract = True

class plaidUser(TimeStampModel):
     catche_id      = models.ForeignKey(User,on_delete=models.CASCADE,default=uuid.uuid4 )
     plaid_id       =models.UUIDField(primary_key=True,editable=False,unique=True,default=uuid.uuid4 )
     access_token   =models.CharField(max_length=50,blank=True)
     created_date   =models.DateTimeField(auto_now_add=True)
   
class plaidUserHistory(TimeStampModel):
    EventID        =models.UUIDField(primary_key=True,editable=False,unique=True,default=uuid.uuid4)
    catche_id      =models.ForeignKey(User,on_delete=models.CASCADE,default=uuid.uuid4)
    plaid_id       =models.ForeignKey(plaidUser,on_delete=models.CASCADE,default=uuid.uuid4)
    access_token   =models.ForeignKey(plaidUser,on_delete=models.CASCADE,related_name='accesstoken',null=True)
    linkReason     =models.CharField(max_length=50,blank=True)
    StartDate      =models.DateTimeField(auto_now_add=True)
    EndDate        =models.DateTimeField(auto_now_add=True)