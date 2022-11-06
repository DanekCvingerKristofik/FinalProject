from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from places.forms import PurchaseForm
from places.models import Trip, Purchase


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
            Q(where_from__name__contains = q) |
            Q(where_to__name__contains = q) |
            Q(where_to__belonging_to_the_country__name__contains=q) |
            Q(where_from__belonging_to_the_country__name__contains=q)
        )
        context = {"query": q, "trips" : trips}
        return render(request, "places/search.html", context)

class PurchaseCreateView(LoginRequiredMixin,CreateView):
    template_name = 'places/purchase_form.html'
    form_class = PurchaseForm

    def post(self, request, *args, **kwargs):
        print(request.POST)
        trip = request.POST.get("trip")[0]
        amount_children = request.POST.get('amount_children')[0]
        amount_adults = request.POST.get('amount_children')[0]
        user = request.user
        Purchase.objects.create(trip_id = trip, user = user, amount_adults = amount_adults, amount_children = amount_children)
        return redirect("your_purchase")


class SignUpView(CreateView):
    template_name = "accounts/signup.html"
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

def your_purchase(request):
    purchase = Purchase.objects.filter(user = request.user).last()
    context = {"purchase": purchase}
    return render(request, "places/your_purchase.html", context)
