from django.db import models
from users.models import User


class UserFlights(models.Model):
    carrier = models.CharField(max_length=10)
    departureDate = models.CharField(max_length=30)
    departureTime = models.CharField(null=True, max_length=30)
    departurePlace = models.CharField(max_length=20)
    duration = models.CharField(max_length=10)
    stops = models.IntegerField(null=True)
    arrivalDate = models.CharField(max_length=30)
    arrivalTime = models.CharField(null=True, max_length=30)
    arrivalPlace = models.CharField(max_length=20)
    price = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
