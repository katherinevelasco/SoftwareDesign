from django.test import TestCase
from django.contrib.auth.models import User
from .models import ClientProfile



# Create your tests here.



class Test_Profile(TestCase):

    def test_statuscode(self):
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)

    def test_template(self):
        response = self.client.get('/profile/')
        self.assertTemplateUsed(response, 'accounts/profile.html')



class Test_editprofile(TestCase):

    def setUp(self):
        # Create one user profile
        test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')

        test_user1.Clientprofile.Full_Name = 'testuser1',
        test_user1.Clientprofile.Address1 = 'testaddress',
        test_user1.Clientprofile.City = 'testCity',
        test_user1.Clientprofile.State = 'testState',
        test_user1.Clientprofile.Zipcode = 'Testcode'

        test_user1.save()

    def test_get(self):
        self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get('/edit_profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/edit_profile.html')

    def test_post(self):
        self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.post('/edit_profile/', {
            'Full_Name': 'test',
            'Address1': 'test',
            'City': 'test',
            'State': 'AR',
            'Zipcode': 'test'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/profile/')
        var = User.objects.get(username='testuser1')
        self.assertEqual(var.Clientprofile.Full_Name, 'test')
        self.assertEqual(var.Clientprofile.Address1, 'test')
        self.assertEqual(var.Clientprofile.City, 'test')
        self.assertEqual(var.Clientprofile.State, 'AR')
        self.assertEqual(var.Clientprofile.Zipcode, 'test')


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
