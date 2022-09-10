from django import forms
from .models import SLTLoan,SlT_Payment_summary


from functools import partial
DateInput = partial(forms.DateInput, {'class': 'datepicker'})



class SLTLoanForm(forms.ModelForm):
 
    Due_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='Due Date'
    )
    class Meta():
        model = SLTLoan
        fields = ('Loan_Type','PaymentDue_amount','Due_date','company_name')

    def __init__(self, *args, **kwargs):
        super(SLTLoanForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['readonly'] = ' '
       
class SlT_Payment_summaryForm(forms.ModelForm):
    Due_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='Due Date'
    )
    class Meta():
        model = SlT_Payment_summary
        fields = ('Loan_Type','PaymentDue_amount','Due_date','Planned_payment','user_payment','cathe_fund','fund_return_date')

    def __init__(self, *args, **kwargs):
        super(SlT_Payment_summary, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['readonly'] = ' '