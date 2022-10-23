
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

    @property
    def length_of_stay(self):
        return self.return_date - self.departure_date


class Purchase(Model):
    trip = models.ForeignKey(City, on_delete=models.CASCADE, related_name="airports")
    amount_adults = models.BigIntegerField()
    amount_children = models.BigIntegerField()
    unit_price_adult = models.BigIntegerField()
    unit_price_child = models.BigIntegerField()


    @property
    def total_price(self):
        return (self.amount_adults * self.unit_price_adult) + (self.amount_children * self.unit_price_child)



