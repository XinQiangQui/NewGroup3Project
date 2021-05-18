from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    name = models.CharField(max_length=20, null=True)
    lastname = models.CharField(max_length=20, null=True)
    email = models.EmailField(max_length=254, null=True)
    phone_number = models.IntegerField(null=True)
    home_address = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=20, default="123")
    status = models.CharField(max_length=20, null=True)


class Supervisor(Account):
    Account.status = 'Supervisor'


class Instructor(Account):
    Account.status = 'Instructor'


class TA(Account):
    Account.status = 'TA'


# course and lab class
class Course(models.Model):
    name = models.CharField(max_length=30)
    cId = models.IntegerField(null=True)
    semester = models.CharField(max_length=20, null=True)
    instructor = Account


class Lab(models.Model):
    lab_name = models.CharField(max_length=30, null=True)
    lab_id = models.IntegerField(null=True)
    TA = None


class Assignment(models.Model):
    name = models.CharField(max_length=50, null=True)
    startDate = models.DateField( null=True)
    endDate = models.DateField( null=True)
    f = None

