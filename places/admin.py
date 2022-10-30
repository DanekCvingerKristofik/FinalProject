from django.contrib import admin

from places.models import Country, City, Hotel, Airport, Trip, Purchase
class CityAdmin(admin.ModelAdmin):
    list_display = ["name", "belonging_to_the_country"]
    list_filter = ["belonging_to_the_country"]



# Register your models here.
admin.site.register(Country)
admin.site.register(City,CityAdmin)
admin.site.register(Hotel)
admin.site.register(Airport)
admin.site.register(Trip)
admin.site.register(Purchase)

