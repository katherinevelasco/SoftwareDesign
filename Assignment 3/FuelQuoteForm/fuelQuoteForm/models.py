from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class userFuelForm(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="related user")
    gallsRequested = models.IntegerField('Gallons Requested', default=0)
    deliveryAddress = models.CharField('Delivery Address', max_length=100)
    deliveryDate = models.DateTimeField('Delivery Date')
    suggPrice = models.IntegerField('Suggested Price', default=0)
    total = models.DecimalField('Total (Price * Gallons)', decimal_places=2,
                                max_digits=9, default=0.00000000 )  # total will be calculated by (suggPrice*gallsRequested)

    def create_quote(sender, **kwargs):
        if kwargs['created']:
            user_quote = userFuelForm.objects.create(user=kwargs['instance'])

    post_save.connect(create_quote, sender= User)


