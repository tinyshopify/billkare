from django import forms
from .models import customer_loan_decision_attrs,customerLoan,user_uploaded_statments


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
       
class user_uploaded_statmentsForm(forms.ModelForm):
    class Meta():
        model=user_uploaded_statments
        fields =('Upload_statement',)
    def __init__(self, *args, **kwargs):
        super(user_uploaded_statmentsForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].label  = 'Upload Bank Statement(optional)[only pdf]'
            self.fields[field].helptext= 'Upload only pdf'
            