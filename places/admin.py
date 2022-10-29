from django.contrib import admin

from places.models import Country, City, Hotel, Airport, Trip, Purchase

# Register your models here.
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Hotel)
admin.site.register(Airport)
admin.site.register(Trip)
admin.site.register(Purchase)

