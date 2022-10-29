from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect

from places.models import Trip, Country


# Create your views here.

def home(request):
     q = request.GET.get('dest', ' ')
     if q == ' ':
          return HttpResponse("Zadejte co chcete hledat")
     else:
          trips = Country.objects.filter(name = q)
          context = {"trips" : trips}
          return render(request, "places/home.html", context)

def trip(request, id):
     trip = Trip.objects.get(id=id)
     context = {'trip': trip}
     return render(request, 'places/trip.html', context)