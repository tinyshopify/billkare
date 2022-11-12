from email import message
from Loan.loanfunctions import get_total_avail_currrent_balance, put_customerLoan

import plaidlink
from .models import User
from plaidlink.models import  plaidUser
from Loan.models import PaymentSummary, customer_loan_decision_attrs, customer_loan_decision_attrs_active, customer_loan_decision_attrs_history

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
                            1800, 
                            '2022-10-26',
                            370,
                            '2022-10-26',
                            900,
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
                            2000, 
                            '2022-10-26',
                            0,
                            None,
                            1000,
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
                            900, 
                            '2022-10-26',
                            0,
                            None,
                            1100,
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
                        3:(3700,'mortgage',1500,'2022-10-26',480,'2022-10-26',260,7220,'2022-10-26','Y',0,0,4000,300,'2022-09-26',10,0,'2022-10-27'),
                        4:(1700,'Auto',1600,'2022-10-26',400,'2022-10-26',950,6100,'2022-10-26','Y',0,0,2300,500,'2022-09-26',20,0,'2022-10-27'),
                        5:(4000,'Credit',1200,'2022-10-26',450,'2022-10-26',800,4110,'2022-10-26','Y',0,0,4200,200,'2022-09-26',60,0,'2022-10-27'),
                        6:(4000,'mortgage',1350,'2022-10-26',420,'2022-10-26',1000,3360,'2022-10-26','Y',0,0,4500,500,'2022-09-26',40,0,'2022-10-27'),
                        7:(1000,'Auto',2450,'2022-10-26',350,'2022-10-26',1150,6800,'2022-10-26','Y',0,0,1150,150,'2022-09-26',30,0,'2022-10-27'),
                        8:(4500,'Credit',900,'2022-10-26',320,'2022-10-26',1370,3560,'2022-10-26','Y',0,0,4650,150,'2022-09-26',50,0,'2022-10-27'),
                        9:(1700,'mortgage',2550,'2022-10-26',410,'2022-10-26',1280,6130,'2022-10-26','Y',0,0,2000,300,'2022-09-26',20,0,'2022-10-27'),
                        10:(1700,'',0,None,0,None,0,0,None,'Y',0,0,0,0,None,20,0,None)
                    }
   return dict(testData)

def get_customer_data(id):

    obj=plaidUser.objects.get(catche_id_id=id)
    accessToken=obj.access_token
    xs,xs1=plaidlink.common.getAccountsDetails(accessToken)
    # print("xs1:",xs1)
    xs2=[ i.split("|") for i in xs1]
    # print("xs2:",xs2[1])
    xs3=[[i[10],i[9],i[8],i[7],i[1],i[2]] for i in xs2[1:]]
    # print(xs3) 
    for i in xs2[1:]:
        account_id=i[0]
        available=float(0 if i[1] == 'None' else i[1] )
        current=float(0 if i[2] == 'None' else i[2] )
        iso_currency_code=i[3]
        limit=i[4]
        unofficial_currency_code=i[5]
        mask=i[6]
        name=i[7]      
        official_name=i[8]
        subtype=i[9]
        type  =i[10]
        customer_loan_decision_attrs_active.objects.update_or_create(
            catche_id_id=id,
            plaid_id_id=obj.plaid_id,
            access_token=accessToken,
            account_id= account_id,
            available_balance=available,
            current_balance=current,
            iso_currency_code=iso_currency_code,
            limit= limit,
            unofficial_currency_code=unofficial_currency_code,
            mask=mask,
            name=name,
            official_name= official_name,
            subtype=subtype,
            type  = type, creUser="live_user",
            InsUpdFlag ='I',
        )
        customer_loan_decision_attrs_history.objects.update_or_create(
            catche_id_id=id,
            plaid_id_id=obj.plaid_id,
            access_token=accessToken,
            account_id= account_id,
            available_balance=available,
            current_balance=current,
            iso_currency_code=iso_currency_code,
            limit= limit,
            unofficial_currency_code=unofficial_currency_code,
            mask=mask,
            name=name,
            official_name= official_name,
            subtype=subtype,
            type  = type, creUser="live_user",
            InsUpdFlag ='I',
        )
    put_customerLoan(id)
    total_avail_balance,total_current_balance=get_total_avail_currrent_balance(id)
    try:
            s=get_customer_loan_decision_attrs(id)  
    except customer_loan_decision_attrs.DoesNotExist:
            customer_loan_decision_attrs.objects.create(catche_id_id=id,
            balance=total_current_balance,
            loan_eligiblity_flag="yes",  estimated_balance=0.0,
            shortage_bill_amount=0.0,)
    return