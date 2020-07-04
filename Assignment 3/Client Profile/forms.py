from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from .models import ClientProfile




class EditClientForm(UserChangeForm):

    class Meta:
        model = ClientProfile

        fields = (
            'Full_Name',
            'Address1',
            'Address2',
            'City',
            'State',
            'Zipcode'
        )

       # def save(self, commit=True):
       # user = super(EditProfileForm, self).save(commit=False)

       #  if commit:
        #    user.save()
     #   return user