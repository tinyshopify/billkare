
from .models import Subscription,CatcheSubscriptionlookup,SubscriptionHistory
import datetime

dt=datetime.datetime.utcnow()

def addmembership(id,membership,username):
     print("add membership",id,membership,username)
     try:
          s=Subscription.objects.get(catche_id_id=id)
          s.SubscriptionType_id=membership.Subscription_Type
          s.creUser         =username
          s.CreatedTs       =dt
          s.UpdateTs        =dt
          s.InsUpdFlag =  "U"
          s.save()
          reason="Update"
          obj=Subscription.objects.get(catche_id_id=id)
          print("subcription",obj)
          insertSubscriptionHistory(id,obj,reason,username)
          
     except Subscription.DoesNotExist:
         s=Subscription.objects.update_or_create(catche_id_id=id,
               SubscriptionType_id=membership.Subscription_Type, 
               # SubscriptionStartDate=None,
               # SubscriptionEndDate=null,
               creUser         =username,
               InsUpdFlag =  "I")
         reason="Create"
         print("create")
         obj=Subscription.objects.get(catche_id_id=id)
         print("subcription",obj)
         insertSubscriptionHistory(id,obj,reason,username)

def cancelmembership(id,username): 
     obj=CatcheSubscriptionlookup.objects.get(Subscription_Type=1)
     try:
          s=Subscription.objects.get(catche_id_id=id)
          s.SubscriptionType_id=obj.Subscription_Type
          s.save()
          reason="Cancel"
          insertSubscriptionHistory(id,s,reason,username)
          message="you currently having a free membership"   
     except Subscription.DoesNotExist:
          message="Memebrship Not found"
     return message

def get_base(membership):
    try:
          obj=CatcheSubscriptionlookup.objects.get(Subscription_Type=membership)
          print(obj)
          return obj
    except CatcheSubscriptionlookup.DoesNotExist: return None

def get_membership(id):
     try:
          s=Subscription.objects.get(catche_id_id=id)
     except Subscription.DoesNotExist:
         return None
     return s.SubscriptionType_id

def insertSubscriptionHistory(id,s,reason,username):
    
     if reason =='Create':
          Subscription_Reason=reason
          Refund_Amount=0
          CreatedTs =dt
          UpdateTs=dt
          InsUpdFlag="I"
     elif reason == 'Update':
         Subscription_Reason=reason
         Refund_Amount=0
         CreatedTs =dt
         UpdateTs   =dt
         InsUpdFlag="U"
     elif reason == 'Cancel':
         Subscription_Reason=reason
         Refund_Amount=0
         CreatedTs =dt
         UpdateTs   =dt
         InsUpdFlag="U"
   
     instance=SubscriptionHistory.objects.create(
          SubscriptionID_id=s.SubscriptionID,
          catche_id_id    = id,
          SubscriptionType_id=s.SubscriptionType_id,
          Subscription_Reason=Subscription_Reason,
          SubscriptionStartDate=s.SubscriptionStartDate,
          SubscriptionEndDate=s.SubscriptionEndDate,
          Refund_Amount=Refund_Amount,
          creUser         =username,
          CreatedTs       =CreatedTs,
          UpdateTs        =UpdateTs,
          InsUpdFlag =  InsUpdFlag,)
