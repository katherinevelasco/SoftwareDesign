from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import userFuelForm
from .forms import FuelQuoteForm


# Create your views here.
def fqf(request):
    if request.method == 'POST':
        form = FuelQuoteForm(request.POST, instance=request.user.userFuelForm)

        if form.is_valid():
            form.save()
            return redirect('fqf')

    form = FuelQuoteForm(instance=request.user)
    return render(request=request,
                  template_name="fuelQuoteForm/fuelform.html",
                  context={"form": form})
