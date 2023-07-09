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
