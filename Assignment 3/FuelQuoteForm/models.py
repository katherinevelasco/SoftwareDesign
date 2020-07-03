from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class userFuelForm(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="related user")
    gallsRequested = models.IntegerField('Gallons Requested', default=0)
    deliveryAddress = models.TextField('Delivery Address')
    deliveryDate = models.DateField(u'Delivery Date', help_text=u'Delivery Date')
    suggPrice = models.IntegerField('Suggested Price',default=0)
    total = models.IntegerField('Total (Price * Gallons)',default=0) #total will be calculated by (suggPrice*gallsRequested)

#class pricingModule(models.Model):
