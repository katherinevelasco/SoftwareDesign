from django import forms
from .models import UserFuelForm

class DateInput(forms.DateInput):
    input_type = 'date'

class FuelQuoteForm(forms.ModelForm):
    class Meta:
        model = UserFuelForm
        fields = (
            "gallsRequested",
            "deliveryAddress",
            "deliveryDate",
            "suggPrice",
            "total",
            "user",
        )
        widgets = {
            "deliveryDate": DateInput(format=('%d-%m-%Y'), attrs={'firstDay':1, 'pattern=': '\d{4}-\d{2}-\d{2}',
                                                               'lang': 'pl', 'format': 'yyyy-mm-dd', 'type': 'date'}),
      }
    def save(self, commit=True):
        user = super(FuelQuoteForm, self).save(commit=False)

        if commit:
            user.save()
        return user
