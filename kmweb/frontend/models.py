from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)


class Ride(models.Model):
    name = models.CharField(max_length=255)
    origin = models.CharField(max_length=255)
    departure_time = models.DateTimeField(null=True, blank=True)
    destination = models.CharField(max_length=255)
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    participants = models.ManyToManyField(User, related_name='rides_participating', blank=True, null=True)