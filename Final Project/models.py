from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from decimal import Decimal


# Create your models here.
class UserProfile(models.Model):
    US_STATES = (('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'),
                 ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'),
                 ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'),
                 ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'),
                 ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'),
                 ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'),
                 ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'),
                 ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'),
                 ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'),
                 ('NY', 'New York'),
                 ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'),
                 ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'),
                 ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'),
                 ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'),
                 ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming'))

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        # verbose_name="related user",
    )
    Full_Name = models.CharField(max_length=50, default='', blank=False)
    Address1 = models.CharField(max_length=100, default='', blank=False)
    Address2 = models.CharField(max_length=100, default='', blank=True)
    City = models.CharField(max_length=100, default='', blank=False)
    State = models.CharField(max_length=5, choices=US_STATES, blank=False)
    Zipcode = models.CharField(max_length=9, blank=False, default='')

    def __str__(self):
        return self.user.username


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)


class UserFuelForm(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="related user")
    gallsRequested = models.IntegerField('Gallons Requested', default=0)
    deliveryAddress = models.CharField('Delivery Address', max_length=100, default='', blank=True)

    deliveryDate = models.DateField()
    suggPrice = models.IntegerField('Suggested Price', default=0)
   # total = models.DecimalField('Total (Price * Gallons)', decimal_places=2,
                               # max_digits=10000,
                               # default=Decimal('0.0000'))  # total will be calculated by (suggPrice*gallsRequested)
    total = models.IntegerField('Total (Price* Gallons)', default=0)


    def __str__(self):
        return self.user.username


class PricingModule(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    currPrice = 1.50

    #locationFactor =
    # suggestedprice = currentprice + margin

    # locationfactor = 2% - texas , 4% - out of state
    # ratehistory = 1% if client requested fuel before, 0% if no history
    # gallrequested - %2 more if > 1000 galls, 3% if less
    # companyprofit = 10% always

    # margin = currentprice * (locationfactor - ratehistory + gallrequested +
    # companyprofit)

    #total = suggPrice * gallsRequested

