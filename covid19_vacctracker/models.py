from django.db import models

class VaccTracker(models.Model):
    lastname = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    contactno = models.CharField(max_length=30)
    barangay = models.CharField(max_length=30)
    streetname = models.CharField(max_length=30)
    house = models.CharField(max_length=10)
    city = models.CharField(max_length=10)
    age = models.CharField(max_length=10)
    birthdate = models.DateField()
    vaccinename = models.CharField(max_length=30)