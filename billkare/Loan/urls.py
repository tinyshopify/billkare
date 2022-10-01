from django.urls import path,include

from . import views

urlpatterns = [
 path('Transaction details/',views.transaction_details,name='transaction_details'),
 path('Loan_page/',views.Loan_page,name='Loan_page'),
 path('connect_bank/',views.connect_bank,name='connect_bank'),
 path('billing_details/',views.billing_details,name='billing_details'),
 path('update_shortage/',views.update_shortage,name='update_shortage'),
 path('Payment_summary/',views.Payment_summary,name='Payment_summary'),
 path('loan_payment/',views.loan_payment,name='loan_payment'),
 path('view_Payment_summary/',views.view_Payment_summary,name='view_Payment_summary'),
 path('cancelPayment/',views. cancelPayment,name='cancelPayment'),
 path('PaymentHistory/',views.PaymentHistory,name='PaymentHistory'),
 path('paymentInfo/',views.paymentInfo,name='paymentInfo'),
   
]