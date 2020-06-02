from django.http import HttpResponse
from django.shortcuts import render
from .models import Flight

# Create your views here.
def index(request):
    #pylint: disable=no-member
    context={
        "flights": Flight.objects.all()
    }
    return render(request,"flights/index.html",context)
