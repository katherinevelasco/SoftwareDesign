from django.shortcuts import render, redirect
from .forms import EditClientForm
from django.contrib import messages
from django.contrib.auth.models import User
from .models import ClientProfile


# Create your views here.


def profile(request):
    form = {'user': request.user}
    return render(request=request,
                  template_name="accounts/profile.html",
                  context={"form": form})


def edit_profile(request):
    if request.method == 'POST':
        form = EditClientForm(request.POST, instance=request.user.clientprofile)

        if form.is_valid():
            form.save()
            return redirect('profile')

    form = EditClientForm(instance=request.user)
    return render(request=request,
                  template_name="accounts/edit_profile.html",
                  context={"form": form})
