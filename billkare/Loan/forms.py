from django import forms
from .models import customer_loan_decision_attrs,customerLoan


from functools import partial
DateInput = partial(forms.DateInput, {'class': 'datepicker'})



class customerLoanForm(forms.ModelForm):
 
    Due_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='Due_date'
    )
    class Meta():
        model = customerLoan
        fields = ('Loan_Type','PaymentDue_amount','days_more')

    def __init__(self, *args, **kwargs):
        super(customerLoanForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['readonly'] = ' '
       
