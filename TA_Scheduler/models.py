from django.db import models
from django.contrib.auth.models import User

# Author : Xin Qiang


# Parent class
class Account(models.Model):
    name = models.CharField(max_length=20, null=True)
    lastname = models.CharField(max_length=20, null=True)
    email = models.EmailField(max_length=254, null=True)
    phone_number = models.IntegerField(null=True)
    home_address = models.CharField(max_length=100, null=True)
    password = "123"
    status = models.CharField(max_length=20, null=True)

    # Getters and setters for all variables
    def get_name(self):
        return self.name

    def set_name(self, newName):
        self.name = newName

    def get_lastname(self):
        return self.lastname

    def set_lastname(self, newLastName):
        self.lastname = newLastName

    def get_email(self):
        return self.email

    def set_email(self, newEmail):
        self.email = newEmail

    def get_phone_num(self):
        return self.phone_number

    def set_phone_num(self, newNum):
        self.phone_number = newNum

    def get_home_address(self):
        return self.home_address

    def set_home_address(self, newAddress):
        self.home_address = newAddress

    def get_password(self):
        return self.password

    def set_password(self, newPassword):
        self.password = newPassword

    def get_status(self):
        return self.status


# Child class
class Supervisor(Account):

    # create a supervisor
    def supervisor(self, name, lastname, email, phone_number, address):
        Account.name = name
        Account.lastname = lastname
        Account.email = email
        Account.phone_number = phone_number
        Account.home_address = address
        Account.status = 'Supervisor'

    # create a course
    def create_course(self, course_name, course_id, startingDate, endingDate,
                      instructor, num_lab, TA_list):
        pass

    # create account
    def create_account(self, account):
        pass

    # delete account
    def delete_account(self, account):
        pass

    # edit account
    def edit_account(self):
        pass

    # send email to users
    def send_email(self, user_list):
        pass

    # assign specific instructor to specific course
    def assign_instructor(self, instructor, course_id):
        pass

    # assign TA to course
    def assign_ta_course(self, TA_list):
        pass

    # assign TA to lab section
    def assign_ta_lab(self, Ta, lab_id):
        pass


class Instructor(Account):
    # create an Instructor
    def instructor(self, name, lastname, email, phone_number, address):
        Account.name = name
        Account.lastname = lastname
        Account.email = email
        Account.phone_number = phone_number
        Account.home_address = address
        Account.status = 'Instructor'

    # edit own contact information
    def edit(self):
        pass

    # display assignment for all TAs
    def display_assignment(self):
        pass

    # send email to TAs
    def send_email(self, TA_list):
        pass

    # assign TA to lab section
    def assign_ta_lab(self, Ta, lab_id):
        pass

    # display public information
    def display(self):
        pass


class TA(Account):
    # create an TA
    def ta(self, name, lastname, email, phone_number, address):
        Account.name = name
        Account.lastname = lastname
        Account.email = email
        Account.phone_number = phone_number
        Account.home_address = address
        Account.status = 'TA'

    # edit own contact information
    def edit(self):
        pass

    # display assignment for all TAs
    def display_assignment(self):
        pass

    # display public information
    def display(self):
        pass

# course and lab class
class Course(models.Model):
    name = models.CharField(max_length=30)
    course_id = models.IntegerField (null=True)
    instructor = None
    ta_list = None
    lab_sections = None

    # getters and setters for course
    def get_name(self):
        return self.name

    def set_name(self, newName):
        self.name = newName

    def get_course_id(self):
        return self.id

    def set_course_id(self, newID):
        self.course_id = newID

    def get_instructor(self):
        return self.instructor

    def set_instructor(self, instructor):
        self.instructor = instructor

    # other methods
    def add_ta(self, Ta):
        pass

    def remove_ta(self, ta):
        pass

    def display_ta(self):
        pass

    def add_lab(self, lab):
        pass

    def remove_lab(self, lab_id):
        pass

    def display_lab(self):
        pass


class Lab(models.Model):
    lab_name = models.CharField(max_length=30, null=True)
    lab_id = models.IntegerField(null=True)
    TA = None

    # getters and setters for course
    def get_lab_name(self):
        return self.lab_name

    def set_lab_name(self, newName):
        self.lab_name = newName

    def get_lab_id(self):
        return self.lab_id

    def set_lab_id(self, newID):
        self.lab_id = newID

    def get_ta(self):
        return self.TA

    def set_ta(self, Ta):
        self.TA = Ta


class Assignment(models.Model):
    topic = models.CharField(max_length=50, null=True)
    startDate = models.DateField( null=True)
    endDate = models.DateField( null=True)
    content = models.CharField(max_length=200, null=True)
    f = None

    def Assignment(self, topic, start, end, content, file):
        self.topic = topic
        self.content = content
        self.startDate = start
        self.endDate = end
        self.f = file

    # getter and setter
    def get_topic(self):
        return self.topic

    def set_topic(self, newTopic):
        self.topic = newTopic

    def get_start_date(self):
        return self.startDate

    def set_start_date(self, newDate):
        self.startDate = newDate

    def get_end_date(self):
        return self.endDate

    def set_end_date(self, newDate):
        self.endDate = newDate

    def edit_content(self):
        pass

    # upload file
    def upload_file(self, file):
        pass


class CourseSection(models.Model):
    """
    Represents an Abstract Course Section (section 201 of CS361) which may have multiple Lab Sections
    associated to it.
    """

    #course_id is bad!!List things from need to input to optional/default
    course_section_id = models.AutoField('Course Section ID', primary_key=True)
    course_section_code = models.CharField('Course Section Code', blank=False, max_length=3)
    lecture_days = models.CharField('Lecture Day(s)', blank=True, max_length=6)
    lecture_time = models.TextField('Lecture Time', blank=True, max_length=12)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, blank=False, help_text="Course ID")
    instructor_id = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True,
                                      help_text="Instructor ID")

    ta_ids = models.ManyToManyField(User, related_name='section_assign', blank=True,
                                    help_text='Ta\'s Assigned to this Course Section')

    class Meta:
        # Adds a unique constraint combination on the two fields
        unique_together = ['course_section_code', 'course_id']

    def __str__(self):
        return f'{self.course_id.course_code} section {self.course_section_code} [{self.instructor_id}]'
