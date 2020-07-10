from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import UserProfile, UserFuelForm

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

    def __init__(self, *args, **kws):
        self.user = kws.pop('user')
        super().__init__(*args, **kws)
        self.fields['user'].initial = self.user
        self.fields["deliveryAddress"].initial = self.user.userprofile.Address1
        self.fields["suggPrice"].initial = 2
        self.fields["total"].initial = 3.00
        self.fields['deliveryAddress'].disabled = True
        self.fields['suggPrice'].disabled = True
        self.fields['total'].disabled = True

        #self.fields['deliveryDate'] =  forms.DateField(input_formats=['%m/%d/%y'])






