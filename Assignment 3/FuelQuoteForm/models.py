from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class userFuelForm(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="related user")
    gallsRequested = models.IntegerField(default=0)
    deliveryAddress = models.CharField(default='', max_length=100)
    deliveryDate = models.IntegerField(default=0)
    suggPrice = models.IntegerField(default=0)
   # total = models.IntegerField(default=gallsRequested*suggPrice)

class pricingModule(models.Model)