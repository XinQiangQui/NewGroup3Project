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


#class Supervisor(Account):
 #   Account.status = 'Supervisor'


#class Instructor(Account):
 #   Account.status = 'Instructor'


#class TA(Account):
 #   Account.status = 'TA'
  #  if request.user.is_superuser:
   #     return redirect('Admin/')
    #elif request.user.role == 'Ta':
     #   return redirect('TAs/')
    #else:
     #   return redirect('Users/')



# course and lab class
class Course(models.Model):
    name = models.CharField(max_length=30)
    cId = models.IntegerField(null=True)
    semester = models.CharField(max_length=20, null=True)
    instructor = Account
    instructorOrTa = models.ForeignKey(Account, blank=True, null=True, on_delete=models.CASCADE)


class LabSection(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    instructorOrTa = models.ForeignKey(Account, blank=True, null=True, on_delete=models.CASCADE)
    number = models.IntegerField()
    meeting_time = models.CharField(max_length=20)
    meeting_location = models.CharField(max_length=20)


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
