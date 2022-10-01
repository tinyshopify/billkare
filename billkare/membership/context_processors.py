from Loan.models import customer_loan_decision_attrs
from .models import Subscription,CatcheSubscriptionlookup

def membership(request):
    data={}
    try:
        if request.user.is_authenticated:
            usermembership=Subscription.objects.get(catche_id_id=request.user.catche_id)
            SubscriptionType =usermembership.SubscriptionType_id
            data['catcheuser']=CatcheSubscriptionlookup.objects.get(Subscription_Type=SubscriptionType)

    except Subscription.DoesNotExist:
         return None
    return dict(data)