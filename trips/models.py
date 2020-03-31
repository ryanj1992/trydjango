from django.db import models
from users.models import User


class UserTrips(models.Model):
    travelLocation = models.CharField(max_length=50)
    totalBudget = models.FloatField()
    startDate = models.DateField()
    endDate = models.DateField()
    description = models.CharField(max_length=255)
    imgUrl = models.CharField(max_length=2083, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
