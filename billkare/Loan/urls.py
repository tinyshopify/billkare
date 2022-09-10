from django.urls import path,include

from . import views

urlpatterns = [
 path('Transaction details/',views.transaction_details,name='transaction_details'),
 path('Loan_page/',views.Loan_page,name='Loan_page'),
 path('connect_bank/',views.connect_bank,name='connect_bank'),
 path('update_shortage/',views.update_shortage,name='update_shortage'),

 path('Eligible_for_fund/<limit>/',views.Eligible_for_fund,name='Eligible_for_fund'),
 path('Eligible_for_fund_cont1/',views.Eligible_for_fund_cont1,name='Eligible_for_fund_cont1'),
 path('Payment_summary/',views.Payment_summary,name='Payment_summary'),
 path('view_Payment_summary/',views.view_Payment_summary,name='view_Payment_summary'),
]