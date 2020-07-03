from django import forms
from django.contrib.auth.models import User


class FuelQuoteForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            "Gallons Requested",
            "Delivery Address",
            "Delivery Date",
            "Suggested Price",
            "Price",
        )

        def save(self, commit=True):
            user = super(FuelQuoteForm, self).save(commit=False)

            if commit:
                user.save()
            return user
