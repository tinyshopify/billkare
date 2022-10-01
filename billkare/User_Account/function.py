from email import message
from .models import User
from plaidlink.models import  plaidUser
from Loan.models import PaymentSummary, customer_loan_decision_attrs

from membership.models import Subscription

def get_user(email):
     user=User.objects.get(email=email)
     return user.catche_id

def get_customer_loan_decision_attrs(id):
     return customer_loan_decision_attrs.objects.get(catche_id_id=id)


def get_payment_summary(id):
     try:
        obj=PaymentSummary.objects.get(catche_id_id=id)
     except PaymentSummary.DoesNotExist:
        return None
     return obj
def is_plaidUser(id):
     try:
        obj=plaidUser.objects.get(catche_id_id=id)
     except  plaidUser.DoesNotExist:
        return False
     return True
def Put_Testdata(catcheid,randomNumber,testData):
                  try :
                        customerLoanAttr = customer_loan_decision_attrs.objects.get(catche_id_id = catcheid)
                        # customerLoanAttr.catche_id_id = catcheid
                        (customerLoanAttr.balance,
                        customerLoanAttr.loanType,
                        customerLoanAttr.mortgage_due_amount,
                        customerLoanAttr.mortgage_due_date,
                        customerLoanAttr.auto_loan_amount,
                        customerLoanAttr.auto_due_date,
                        customerLoanAttr.creditcard_min_paydue_amount,
                        customerLoanAttr.creditcard_statment_balance_amount,
                        customerLoanAttr.creditcard_due_date,
                        customerLoanAttr.loan_eligiblity_flag,
                        customerLoanAttr.max_loan_amount_from_catche,
                        customerLoanAttr.min_loan_amount_from_catche,
                        customerLoanAttr.estimated_balance,
                        customerLoanAttr.shortage_bill_amount,
                        customerLoanAttr.paycheck_date,
                        customerLoanAttr.catche_risk_score_0_100,
                        customerLoanAttr.customer_entered_bill_amount,
                        # bilamt for mort
                        # auto credit
                        customerLoanAttr.catche_bill_due_date
                        ) = testData[randomNumber]

                        customerLoanAttr.creUser="live_user",
                        customerLoanAttr.InsUpdFlag ='U'

                        customerLoanAttr.save()

                  except  customer_loan_decision_attrs.DoesNotExist:
                        customerLoanAttr = customer_loan_decision_attrs()
                        customerLoanAttr.catche_id_id = catcheid
                        (customerLoanAttr.balance,
                        customerLoanAttr.loanType,
                        customerLoanAttr.mortgage_due_amount,
                        customerLoanAttr.mortgage_due_date,
                        customerLoanAttr.auto_loan_amount,
                        customerLoanAttr.auto_due_date,
                        customerLoanAttr.creditcard_min_paydue_amount,
                        customerLoanAttr.creditcard_statment_balance_amount,
                        customerLoanAttr.creditcard_due_date,
                        customerLoanAttr.loan_eligiblity_flag,
                        customerLoanAttr.max_loan_amount_from_catche,
                        customerLoanAttr.min_loan_amount_from_catche,
                        customerLoanAttr.estimated_balance,
                        customerLoanAttr.shortage_bill_amount,
                        customerLoanAttr.paycheck_date,
                        customerLoanAttr.catche_risk_score_0_100,
                        customerLoanAttr.customer_entered_bill_amount,
                        customerLoanAttr.catche_bill_due_date
                        ) = testData[randomNumber]

                        customerLoanAttr.creUser="live_user",
                        customerLoanAttr.InsUpdFlag ='I'

                        customerLoanAttr.save()
                  if customerLoanAttr.mortgage_due_amount== 0 and customerLoanAttr.mortgage_due_date==None and customerLoanAttr.auto_loan_amount==0 and customerLoanAttr.auto_due_date==None and customerLoanAttr.creditcard_min_paydue_amount==0 and customerLoanAttr.creditcard_statment_balance_amount==0 and customerLoanAttr.creditcard_due_date==None :
                     message="Congrats! You dont have any Loan Payment"
                     return message



def get_Testdata():
   testData = {
                        0 : (
                            1000, 
                            'mortgage', 
                            250, 
                            '2022-10-26',
                            120,
                            '2022-10-26',
                            150,
                            1000,
                            '2022-10-26',
                            'Y',
                            0,
                            0,
                            1500,
                            500,
                            '2022-09-26',
                            10,
                            0,
                            '2022-10-27'
                            ),
                        1 : (
                            2000, 
                            'mortgage', 
                            250, 
                            '2022-10-26',
                            0,
                            None,
                            150,
                            2000,
                            '2022-10-26',
                            'Y',
                            0,
                            0,
                            2500,
                            500,
                            '2022-09-26',
                            10,
                            0,
                            '2022-10-27'
                            ),
                        2 : (
                            3000, 
                            'Credit Card', 
                            250, 
                            '2022-10-26',
                            0,
                            None,
                            150,
                            2000,
                            '2022-10-26',
                            'Y',
                            0,
                            0,
                            3500,
                            500,
                            '2022-09-26',
                            10,
                            0,
                            '2022-10-27'
                            ),
                        3:(3700,'mortgage',250,'2022-10-26',480,'2022-10-26',260,7220,'2022-10-26','Y',0,0,4000,300,'2022-09-26',10,0,'2022-10-27'),
                        4:(1700,'Auto',500,'2022-10-26',310,'2022-10-26',100,6100,'2022-10-26','Y',0,0,2300,500,'2022-09-26',20,0,'2022-10-27'),
                        5:(4000,'Credit',200,'2022-10-26',400,'2022-10-26',130,4110,'2022-10-26','Y',0,0,4200,200,'2022-09-26',60,0,'2022-10-27'),
                        6:(4000,'mortgage',350,'2022-10-26',220,'2022-10-26',290,3360,'2022-10-26','Y',0,0,4500,500,'2022-09-26',40,0,'2022-10-27'),
                        7:(1000,'Auto',600,'2022-10-26',350,'2022-10-26',330,6800,'2022-10-26','Y',0,0,1150,150,'2022-09-26',30,0,'2022-10-27'),
                        8:(4500,'Credit',150,'2022-10-26',320,'2022-10-26',370,3560,'2022-10-26','Y',0,0,4650,150,'2022-09-26',50,0,'2022-10-27'),
                        9:(1700,'mortgage',250,'2022-10-26',410,'2022-10-26',280,6130,'2022-10-26','Y',0,0,2000,300,'2022-09-26',20,0,'2022-10-27'),
                        10:(1700,'',0,None,0,None,0,0,None,'Y',0,0,0,0,None,20,0,None)
                    }
   return dict(testData)