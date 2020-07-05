from django.contrib import admin
from accounts.models import UserProfile, PricingModule, UserFuelForm

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(UserFuelForm)

admin.site.register(PricingModule)
