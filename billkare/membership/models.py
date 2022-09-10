from django.db import models
import uuid
from User_Account.models import SLTAuth

# Create your models here.

class SLT_membership(models.Model):
     SLT_id= models.ForeignKey(SLTAuth,on_delete=models.CASCADE,default=uuid.uuid4 )
     membership=models.CharField(max_length=50,blank=True)