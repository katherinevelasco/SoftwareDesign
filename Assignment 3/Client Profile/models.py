from django.db import models
from django.contrib.auth.models import User


class ClientProfile(models.Model):

    STATE_CHOICES = (
        (('AL', ('Alabama')),
            ('AZ', ('Arizona')),
            ('AR', ('Arkansas')),
            ('CA', ('California')),
            ('CO', ('Colorado')),
            ('CT', ('Connecticut')),
            ('DE', ('Delaware')),
            ('DC', ('District of Columbia')),
            ('FL', ('Florida')),
            ('GA', ('Georgia')),
            ('ID', ('Idaho')),
            ('IL', ('Illinois')),
            ('IN', ('Indiana')),
            ('IA', ('Iowa')),
            ('KS', ('Kansas')),
            ('KY', ('Kentucky')),
            ('LA', ('Louisiana')),
            ('ME', ('Maine')),
            ('MD', ('Maryland')),
            ('MA', ('Massachusetts')),
            ('MI', ('Michigan')),
            ('MN', ('Minnesota')),
            ('MS', ('Mississippi')),
            ('MO', ('Missouri')),
            ('MT', ('Montana')),
            ('NE', ('Nebraska')),
            ('NV', ('Nevada')),
            ('NH', ('New Hampshire')),
            ('NJ', ('New Jersey')),
            ('NM', ('New Mexico')),
            ('NY', ('New York')),
            ('NC', ('North Carolina')),
            ('ND', ('North Dakota')),
            ('OH', ('Ohio')),
            ('OK', ('Oklahoma')),
            ('OR', ('Oregon')),
            ('PA', ('Pennsylvania')),
            ('RI', ('Rhode Island')),
            ('SC', ('South Carolina')),
            ('SD', ('South Dakota')),
            ('TN', ('Tennessee')),
            ('TX', ('Texas')),
            ('UT', ('Utah')),
            ('VT', ('Vermont')),
            ('VA', ('Virginia')),
            ('WA', ('Washington')),
            ('WV', ('West Virginia')),
            ('WI', ('Wisconsin')),
            ('WY', ('Wyoming')),)
    )
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name="related user",
    )
    FullName = models.TextField(max_length=50, blank=False)
    Address1 = models.TextField(max_length=100, blank=False)
    Address2 = models.TextField(max_length=100, blank=True)
    City = models.TextField(max_length=100, blank=False)
    State = models.CharField(max_length=2, choices=STATE_CHOICES, blank=False)
    ZipCode = models.CharField(max_length=9, blank=False)

