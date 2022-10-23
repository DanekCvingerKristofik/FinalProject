from django.core.management import BaseCommand
import airportsdata


class Command(BaseCommand):

    def handle(self, *args, **options):
        airports = airportsdata.load('IATA')  # key is IATA code
        print(airports)
