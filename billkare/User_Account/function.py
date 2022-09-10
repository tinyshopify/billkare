from User_Account.models import SLT_accesstocken,SLTAuth
from Loan.models import SLTLoan,SlT_summary

from membership.models import SLT_membership

def get_user(email):
     sltauth=SLTAuth.objects.get(email=email)
     return sltauth.sourcelantics_id
def get_summaryobject(id):
     return SlT_summary.objects.get(SLT_id_id=id)

def get_membership(id):
     try:
          s=SLT_membership.objects.get(SLT_id_id=id)
     except SLT_membership.DoesNotExist:
          s=None
     if s== None: return None
     return s.membership