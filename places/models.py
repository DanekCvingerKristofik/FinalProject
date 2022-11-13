from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from django.db.models import Model


class Country(Model):
    name = models.CharField(max_length=50)

    def __str__(self):
       return  f"country: {self.name}"

class City(Model):
    name = models.CharField(max_length=50)
    belonging_to_the_country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="cities")

    def __str__(self):
       return  f" {self.name} "



class Hotel(Model):
    name = models.CharField(max_length=50)
    belonging_to_the_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="hotels")
    stars = models.CharField(max_length=5)
    description = models.CharField(max_length=250)

    def __str__(self):
       return  f" {self.name}"



class Airport(Model):
    name = models.CharField(max_length=50)
    belonging_to_the_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="airports")

    def __str__(self):
       return  f"{self.name}"


class Trip(Model):
    where_from = models.ForeignKey(City, on_delete=models.CASCADE, related_name="from_destination_trips")
    where_to = models.ForeignKey(City, on_delete=models.CASCADE, related_name="to_destination_trips")
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="airport")
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="hotel")
    departure_date = models.DateTimeField()
    return_date =  models.DateTimeField()
    price_for_an_adult = models.BigIntegerField()
    price_for_an_child = models.BigIntegerField()
    number_of_places_for_adults = models.BigIntegerField()
    number_of_places_for_children = models.BigIntegerField()

    bed_breakfast = 'BB'
    half_board = 'HB'
    full_board = 'FB'
    all_inclusive = "AI"
    TYPE_NAME_CHOICES = [
        (bed_breakfast, 'bed & breakfast'),
        (half_board , ' half board'),
        (full_board, 'full board'),
        (all_inclusive , 'all inclusive')
    ]
    type = models.CharField(choices=TYPE_NAME_CHOICES, max_length=2)

    def __str__(self):
       return  f"destination: {self.where_to}"

    @property
    def length_of_stay(self):
        return self.return_date - self.departure_date


class Purchase(Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name="purchases")
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="purchases")
    amount_adults = models.IntegerField()
    amount_children = models.IntegerField()



    @property
    def total_price(self):
        return (self.amount_adults * self.trip.price_for_an_adult) + (self.amount_children * self.trip.price_for_an_child)


class Profil(Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name="profil")
    points = models.IntegerField(default=1000)

    @property
    def add_points(self, points):
        points += 100







