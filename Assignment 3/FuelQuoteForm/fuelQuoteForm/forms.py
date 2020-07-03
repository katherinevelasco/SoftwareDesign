from django import forms
from .models import userFuelForm

class FuelQuoteForm(forms.ModelForm):
    class Meta:
        model = userFuelForm
        fields = (
            "gallsRequested",
            "deliveryAddress",
            "deliveryDate",
            "suggPrice",
            "total",
        )

    def save(self, commit=True):
        user = super(FuelQuoteForm, self).save(commit=False)

        if commit:
            user.save()
        return user
