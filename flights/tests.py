from django.test import TestCase
from flights.models import UserFlights


class FlightTestCase(TestCase):
    def testFlight(self):
        flight = UserFlights(price="My Title", arrivalTime="Blurb", carrier="Post Body")
        self.assertEqual(flight.price, "My Title")
        self.assertEqual(flight.arrivalTime, "Blurb")
        self.assertEqual(flight.carrier, "Post Body")
