from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.

class userFuelForm(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="related user")
    gallsRequested = models.IntegerField('Gallons Requested', default=0)
    deliveryAddress = models.TextField('Delivery Address')
    deliveryDate = models.DateField(u'Delivery Date')
    suggPrice = models.DecimalField('Suggested Price', decimal_places=2, max_digits=10000)
    total = models.DecimalField('Total (Price * Gallons)', decimal_places=2,
                                max_digits=10000)  # total will be calculated by (suggPrice*gallsRequested)

    def create_quote(sender, **kwargs):
        if kwargs['created']:
           user_quote = userFuelForm.objects.create(user=kwargs['instance'])

    post_save.connect(create_quote, sender= User)
