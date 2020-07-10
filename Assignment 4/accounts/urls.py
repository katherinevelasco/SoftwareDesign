
from django.urls import path
from . import views 


urlpatterns = [
    path('', views.home, name = 'accounts-home'),
    #path('login/', views.loginView, name= 'mylogin'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_request, name='logout'),
    path('login/', views.login_request, name= 'login'),
    path('profile/', views.profile, name= 'profile'),
    path('edit_profile/', views.edit_profile, name= 'edit_profile'),
    path('fuelhistory/', views.fuelhistory, name= 'fuelhistory'),
    path('fuelform/', views.fqf, name = 'fuelform'),

]