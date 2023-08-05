from django.db import models


# Create your models here.
# SQl database are divided into different categories: MySQl, SQlite


class Users(models.Model):
    fname = models.CharField(max_length=25, blank=False, null=False)
    onames = models.CharField(max_length=25, blank=False, null=False)
    phone = models.IntegerField()
    dob = models.CharField(max_length=25, blank=False, null=False)
    email = models.EmailField()
    country = models.CharField(max_length=25, blank=False, null=False)
    gender = models.CharField(max_length=6, blank=False, null=False)

    def __str__(self):
        return self.name


class Messages(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    phone = models.IntegerField()
    subject = models.CharField(max_length=50, blank=False, null=False)
    message = models.CharField(max_length=250, blank=False, null=False)

    def __str__(self):
        return self.name


class Uploadfiles(models.Model):
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    file = models.FileField(upload_to="uploaded_files/", blank=True, null=True)

    def __str__(self):
        return self.image


class Shop(models.Model):
    make = models.CharField(max_length=20, null=False, blank=False)
    model = models.CharField(max_length=20, null=False, blank=False)
    cc = models.IntegerField()
    mileage = models.IntegerField()
    fuel_type = models.CharField(max_length=10, null=False, blank=False)
    transmission = models.CharField(max_length=20, null=False, blank=False)
    year = models.IntegerField()
    color = models.CharField(max_length=20, null=False, blank=False)
    available_units = models.IntegerField()
    photo = models.ImageField(upload_to="shopvehicles/", blank=True, null=True)
    price = models.IntegerField()

    # other_photos = models.ImageField(upload_to='shopvehicles/', blank=True, null=True)


    def __str__(self):
        return self.make

