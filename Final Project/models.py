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
        ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'),
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
    Full_Name =models.CharField(max_length=50, default='', blank = False)
    Address1 = models.CharField(max_length=100, default='', blank=False)
    Address2 = models.CharField(max_length=100, default='', blank= True)
    City = models.CharField(max_length=100, default='', blank = False)
    State = models.CharField(max_length=5, choices=US_STATES, blank=False) 
    Zipcode = models.CharField(max_length=9, blank=False, default='')
    def __str__(self):
        return self.user.username

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender= User)


class UserFuelForm(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="related user")
    gallsRequested = models.IntegerField('Gallons Requested', default=1)
    deliveryAddress = models.CharField('Delivery Address', max_length=100, default='', blank= True)

    deliveryDate =  models.DateField()
    suggPrice = models.IntegerField('Suggested Price', default=0)
    total = models.DecimalField('Total (Price * Gallons)', decimal_places=15,
                                max_digits=10000, default=Decimal('0.0000'))  # total will be calculated by (suggPrice*gallsRequested)
  
    def __str__(self):
        return self.user.username
    
 


class PricingModule:
    def __init__(self, galls_req, user):
        self.current_price = 1.50
        self.galls_requested = galls_req
        self.user = user

    def state_factor(self):
        if self.user.userprofile.State == 'TX':
            return 0.02
        else:
            return 0.04

    def rate_history_factor(self):
        doesHistoryExist = UserFuelForm.objects.filter(user=self.user).exists()

        if doesHistoryExist:
            return 0.01 
        else:
            return 0.0

    def galls_requested_factor(self):
        if int(self.galls_requested) > 1000:
            return 0.2
        else:
            return 0.3

    def margin(self):
        location_factor = self.state_factor()
        rate_history_factor = self.rate_history_factor()
        galls_requested_factor = self.galls_requested_factor()

        company_profit_factor = 0.10

        margin = self.current_price * (location_factor - rate_history_factor + galls_requested_factor + company_profit_factor)

        return margin
    
    def calculate(self):
        
        result = self.margin() * self.galls_requested
        return result



