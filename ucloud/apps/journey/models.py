from django.db import models

# Create your models here.
class Story(models.Model):
    fname = models.CharField(max_length=30)
    mname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    lname2 = models.CharField(max_length=30)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    ethnicity = models.CharField(max_length=30)
    ethnicity2 = models.CharField(max_length=30)
    ethnicity3 = models.CharField(max_length=30)
    ethnicity4 = models.CharField(max_length=30)
    ethnicity5 = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50)
    address3 = models.CharField(max_length=50)
    town = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
