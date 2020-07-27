from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm,  AuthenticationForm , UserChangeForm   
from django.contrib.auth import logout, authenticate, login
from .forms import RegistrationForm, EditProfileForm, FuelQuoteForm
from django.contrib import messages
from django.contrib.auth.models import User
from .models import UserProfile, UserFuelForm, PricingModule

# Create your views here.

def home(request):
    return render(request, 'accounts/home.html')

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            
            login(request, user)
            return redirect('login')

        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(request = request,
                          template_name = "accounts/register.html",
                          context={"form":form})

    form = RegistrationForm()
    return render(request = request,
                  template_name = "accounts/register.html",
                  context={"form":form})

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('accounts-home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    #get
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "accounts/login.html",
                    context={"form":form})
    print(form.errors)

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('login')


def profile(request):
    form = {'user': request.user}
    return render(request = request,
                template_name = "accounts/profile.html",
                context={"form":form})

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance = request.user.userprofile)
    
        if form.is_valid():
            form.save()                   
            return redirect('profile')

    form = EditProfileForm(instance=request.user)
    return render(request = request,
            template_name = "accounts/edit_profile.html",
            context={"form":form})


def fqf(request):
    if request.method == 'POST':
        form = FuelQuoteForm(request.POST, user = request.user)
        if not form.is_valid():
            print("something didnt work")
            #getrid
                # allObj = UserFuelForm.objects.all()
                # userObj = UserFuelForm.objects.filter(user = request.user)
                # if UserFuelForm.objects.filter(user = request.user).exists():
                #     # at least one object satisfying query exists
                #     print(userObj)
                #     PricingModule.RateHistoryFactor = 1.0
                # else:
                #     PricingModule.RateHistoryFactor = 2.0
                #     print("user does not have any history")
                #     # no object satisfying query exists
                # print(allObj)
                # print(userObj)
        print(request.POST.keys())
        
        if 'get_quote' in request.POST.keys():
            # Get quote button was pressed
            return render(request=request,
                    template_name="accounts/fuelform.html",
                    context={"form": form})
        else:
            form.save()
            return redirect('profile')

    elif request.method == 'GET':
        form = FuelQuoteForm(user=request.user)
        return render(request=request,
                    template_name="accounts/fuelform.html",
                    context={"form": form})


def fuelhistory(request):
    history = UserFuelForm.objects.filter(user = request.user)
    return render(request, 'accounts/fuelhistory.html', context={"history": history})

