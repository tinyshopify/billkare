from django import forms
from .models import customer_loan_decision_attrs


from functools import partial
DateInput = partial(forms.DateInput, {'class': 'datepicker'})



class SLTLoanForm(forms.ModelForm):
 
    Due_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='Due Date'
    )
    class Meta():
        model = customer_loan_decision_attrs
        fields = ('loanType',)

    def __init__(self, *args, **kwargs):
        super(SLTLoanForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['readonly'] = ' '
       
