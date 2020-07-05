from django.test import TestCase
from django.test import RequestFactory
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,  AuthenticationForm , UserChangeForm   
from .models import UserProfile, UserFuelForm
from .forms import RegistrationForm



# Create your tests here.
class Test_home(TestCase):

    def test_statuscode(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'accounts/home.html')

class Test_fuelhistory(TestCase):

    def test_statuscode(self):
        response = self.client.get('/fuelhistory/')
        self.assertEqual(response.status_code, 200)

    def test_template(self):
        response = self.client.get('/fuelhistory/')
        self.assertTemplateUsed(response, 'accounts/fuelhistory.html')
   
class Test_login(TestCase):

    def setUp(self):
        # Create two users
        test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')        
        test_user1.save()

    def test_get(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)
        #self.assertEqual(response.context['form'], AuthenticationForm())

        self.assertTemplateUsed(response, 'accounts/login.html')

    def test_loginSuccess(self):
        response = self.client.post('/login/', {'username': 'testuser1', 'password': '1X<ISRUkw+tuK'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')

    def test_loginUnsuccess(self):
        response = self.client.post('/login/', {'username': 'testuser1', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')
        self.assertContains(response, 'Invalid username or password.')
 
class Test_register(TestCase):


    def test_get(self):
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register.html')

    def test_RegisterSuccess(self):
        response = self.client.post('/register/', {'username': 'testuser2',
        'password1': '1X<ISRUkw+tuK',
        'password2': '1X<ISRUkw+tuK'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/login/')

    def test_RegisterUnsuccess(self):
        response = self.client.post('/register/', {'username':'testuser2',
        'password1':'1X<ISRUkw+tuK',
        'password2': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register.html')


class Test_Profile(TestCase):

    def test_statuscode(self):
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)

    def test_template(self):
        response = self.client.get('/profile/')
        self.assertTemplateUsed(response, 'accounts/profile.html')


class Test_logout(TestCase):

    def test_statuscode(self):
        response = self.client.get('/logout/')
        self.assertEqual(response.status_code, 302)

    def test_template(self):
        response = self.client.get('/logout/')
        self.assertRedirects(response, '/login/')

class Test_editprofile(TestCase):

    def setUp(self):
        # Create one user profile
        test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')   
             
        test_user1.userprofile.Full_Name='testuser1',
        test_user1.userprofile.Address1 ='testaddress', 
        test_user1.userprofile.City = 'testCity',
        test_user1.userprofile.State = 'testState', 
        test_user1.userprofile.Zipcode = 'Testcode'
    
        test_user1.save()
   
    def test_get(self):
        self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get('/edit_profile/')
        self.assertEqual(response.status_code, 200)
        #self.assertEqual(response.context['form'], AuthenticationForm())
        self.assertTemplateUsed(response, 'accounts/edit_profile.html')

    def test_post(self):
        self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.post('/edit_profile/', {
            'Full_Name': 'test', 
            'Address1': 'test', 
            'City':'test', 
            'State': 'AR',
            'Zipcode':'test' })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/profile/')
        var = User.objects.get(username='testuser1')
        self.assertEqual(var.userprofile.Full_Name, 'test')
        self.assertEqual(var.userprofile.Address1, 'test')
        self.assertEqual(var.userprofile.City, 'test')
        self.assertEqual(var.userprofile.State, 'AR')
        self.assertEqual(var.userprofile.Zipcode, 'test')

class Test_fqf(TestCase):
    def setUp(self):
        # Create one user profile
        test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')  
        # test_user1.userfuelform.gallsRequested =2
        test_user1.save()
        # user = test_user1
        # user.gallsRequested = 2
        # user.deliveryDate ='2020-05-03',
        # user.suggPrice = 2,
        # user.deliveryAddress ='testaddress', 
        # user.total = 3.00

               
    def test_get(self):
        self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get('/fuelform/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/fuelform.html')

    def test_post(self):

        self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        print("client logged in")
        var = User.objects.get(username='testuser1')
        response = self.client.post('/fuelform/', {
            'user' : 'testuser1',
            'gallsRequested' : 2,
            'deliveryDate' :'2020-05-03',
            'suggPrice' : 2,
            'deliveryAddress' : var.userprofile.Address1, 
            'total' : 3.00})
        self.assertEqual(response.status_code, 302)
      
        self.assertRedirects(response, '/profile/')
        #var = User.objects.get(username='testuser1')
        # self.assertEqual(var.userfuelform.gallsRequested, 'testgallons')
        # self.assertEqual(var.userfuelform.deliveryDate,'testdate')
        # self.assertEqual(var.userfuelform.suggPrice, 'testprice')
        # self.assertEqual(var.userfuelform.deliveryAddress, 'testaddress')
        # self.assertEqual(var.userfuelform.total, 'testtotal')