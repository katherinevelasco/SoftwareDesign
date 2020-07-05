from django.test import TestCase
from .models import UserFuelForm
from django.contrib.auth.models import User
# Create your tests here.

class Test_fqf(TestCase):
    def setUp(self):
        # Create one user profile
        test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')

        def __init__(self, *args, **kws):
            self.user = kws.pop('test_user1')
            super().__init__(*args, **kws)
            self.fields['user'].initial = self.user
            self.fields["deliveryAddress"].initial = 'testaddress'
            self.fields["gallsRequested"].initial = '2'
            self.fields["deliveryDate"].initial = '2020-5-3'
            self.fields["total"].initial = '3.0'
            self.fields["suggPrice"].initial = '2'

        test_user1.save()

    def test_get(self):
        self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get('fuelform/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'fuelQuoteForm/fuelform.html')

    def test_post(self):
        self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.post('/fuelform/', {
            'user': 'test',
            'deliveryAddress': 'test',
            'gallsRequested': 'test',
            'deliveryDate': 'test',
            'total': 'test',
            'suggPrice': 'test'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/fuelform')
        var = UserFuelForm.objects.get(username='testuser1')
        self.assertEqual(var.userprofile.user, 'test')
        self.assertEqual(var.userprofile.deliveryAddress, 'test')
        self.assertEqual(var.userprofile.gallsRequested, 'test')
        self.assertEqual(var.userprofile.deliveryDate, 'test')
        self.assertEqual(var.userprofile.total, 'test')
        self.assertEqual(var.userprofile.suggPrice, 'test')




