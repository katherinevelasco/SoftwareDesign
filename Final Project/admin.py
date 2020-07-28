from django.contrib import admin
from .models import UserProfile, PricingModule, UserFuelForm

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(UserFuelForm)

#admin.site.register(PricingModule)
#delete above code because PricingModule is just a class