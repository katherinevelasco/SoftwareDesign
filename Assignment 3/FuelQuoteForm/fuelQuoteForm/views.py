from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def fqf(request):
    return render(request, 'fuelform.html')
