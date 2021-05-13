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


# course and lab class
class Course(models.Model):
    name = models.CharField(max_length=30)
    cId = models.IntegerField(null=True)
    semester = models.CharField(max_length=20, null=True)
    instructor = None


class LabSection(models.Model):
    lab_name = models.CharField(max_length=30, null=True)
    lab_id = models.IntegerField(null=True)
    TA = None


class Assignment(models.Model):
    topic = models.CharField(max_length=50, null=True)
    startDate = models.DateField(null=True)
    endDate = models.DateField(null=True)
    content = models.CharField(max_length=200, null=True)
    f = None


class PersonalInfo(models.Model):
    instructorOrTa = models.ForeignKey(Account, blank=True, null=True, on_delete=models.CASCADE)
    office = models.CharField(max_length=20, blank=True, null=True)
    phone_num = models.IntegerField(blank=True, null=True)
    office_hours = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=20, blank=True, null=True)
