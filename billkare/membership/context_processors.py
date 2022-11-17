from Loan.models import customer_loan_decision_attrs
from .models import Subscription,SuganSubscriptionlookup

def membership(request):
    data={}
    try:
        if request.user.is_authenticated:
            usermembership=Subscription.objects.get(Sugan_id_id=request.user.Sugan_id)
            SubscriptionType =usermembership.SubscriptionType_id
            data['Suganuser']=SuganSubscriptionlookup.objects.get(Subscription_Type=SubscriptionType)

    except Subscription.DoesNotExist:
         return None
    return dict(data)