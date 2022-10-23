
from django.db import models

# Create your models here.
from django.db.models import Model


class Country(Model):
    name = models.CharField(max_length=50)


class City(Model):
    name = models.CharField(max_length=50)
    belonging_to_the_country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="cities")



class Hotel(Model):
    name = models.CharField(max_length=50)
    belonging_to_the_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="hotels")
    stars = models.CharField(max_length=5)
    description = models.CharField(max_length=250)


class Airport(Model):
    name = models.CharField(max_length=50)
    belonging_to_the_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="airports")


class Trip(Model):
    where_from = models.CharField(max_length=50)
    where_to = models.CharField(max_length=50)
    departure_date = models.DateTimeField()
    return_date =  models.DateTimeField()
    length_of_stay = return_date - departure_date
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
    type = models.CharField(choices=TYPE_NAME_CHOICES, max_length=2, unique=True)


class Purchase(Model):
    trip = models.ForeignKey(City, on_delete=models.CASCADE, related_name="airports")
    amount_adults = models.BigIntegerField()
    amount_children = models.BigIntegerField()
    unit_price_adult = Trip.price_for_an_adult
    unit_price_child = Trip.price_for_an_child
    total_price = (amount_adults * unit_price_adult) + (amount_children * unit_price_child)




