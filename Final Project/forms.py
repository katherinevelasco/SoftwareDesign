from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import UserProfile, UserFuelForm, PricingModule
from decimal import Decimal

class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
                "username",
                "password1", 
                "password2", 
            )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        
        if commit:
            user.save()
        return user

class EditProfileForm(UserChangeForm):

    class Meta:
        model = UserProfile

        fields = (
            'Full_Name',
            'Address1', 
            'Address2', 
            'City', 
            'State',
            'Zipcode'
        )
class DateInput(forms.DateInput):
    input_type = 'date'

class FuelQuoteForm(forms.ModelForm):
    suggPrice = forms.DecimalField(max_digits = 6, decimal_places = 5)
    total = forms.DecimalField(max_digits = 6, decimal_places = 5)

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
        'deliveryDate': forms.DateInput(format=('%m/%d/%Y'), attrs={ 'placeholder':'Select a date', 'type':'date'}),
        }

    def clean_suggPrice(self):
        galls = self.cleaned_data['gallsRequested']
        user =  self.fields['user'].initial
        module = PricingModule(galls, user)

        sugg_price = module.margin()
        print("SUGG1", sugg_price)

        final_sugg_price = Decimal(sugg_price + 1.5)
        round_sugg_price = round(final_sugg_price, 3)

        self.fields['suggPrice'].initial = round_sugg_price

        print("SUGG2", round_sugg_price)
        return round_sugg_price

    def clean_total(self):
        galls = self.cleaned_data['gallsRequested']
        user =  self.fields['user'].initial
        module = PricingModule(galls, user)
        dec_total = Decimal(module.calculate())
        total = round(dec_total, 3)
        self.fields['total'].initial = total
        print("total", total)
        return total
    
    # def set_total(self):
    #     galls = self.cleaned_data['gallsRequested']
    #     user =  self.fields['user'].initial
    #     module = PricingModule(galls, user)
    #     self.cleaned_data['suggPrice'] = round(module.margin(), 3)
    #     #self.fields['total'].initial = round(module.calculate(), 3)
    #     #self.cleaned_data['total'] = round(module.calculate(), 3)
    #     total = round(module.calculate(), 3)
    #     self.fields['total'].initial = total
    #     print("total", total)
    #     return total


    def __init__(self, *args, **kws):
        self.user = kws.pop('user')
        super().__init__(*args, **kws)
        self.fields['user'].initial = self.user
        self.fields["deliveryAddress"].initial = self.user.userprofile.Address1
        self.fields["suggPrice"].initial = 0.0
        self.fields["total"].initial = 0.0
        self.fields["gallsRequested"].initial = 1.0
        self.fields['deliveryAddress'].disabled = True
        self.fields['suggPrice'].disabled = True
        self.fields['total'].disabled = True

        






