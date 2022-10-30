from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect

from places.models import Trip, Country


# Create your views here.


def home(request):
     dest = request.GET.get("dest")
     if dest:
          trips = Trip.objects.filter(where_to__belonging_to_the_country__name= dest)

     else:
          trips = Trip.objects.all()
     context = {"trips" : trips}
     return render(request, "places/home.html", context)


def trip(request, id):
      trip = Trip.objects.get(id =id)
      context = {'trip': trip}
      return render(request, 'places/trip.html', context)

def search(request):
    q = request.GET.get('q', ' ')
    if q == ' ' :
        return HttpResponse("Zadejte co chcete hledat")
    else:
        trips = Trip.objects.filter(
            Q(where_from__contains = q) |
            Q(where_to__contains= q)|
            Q(departure_date__contains= q) |
            Q(return_date__contains= q) |
            Q(type__contains= q) |
            Q(length_of_stay__contains= q)
        )
        context = {"query": q, "trips" : trips}
        return render(request, "places/search.html", context)