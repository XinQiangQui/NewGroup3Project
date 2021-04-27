from django.db import models


# Author : Xin Qiang


# Parent class
class Account(models.Model):
    name = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    phone_number = models.IntegerField()
    home_address = models.CharField(max_length=100)
    status = models.CharField(max_length=10)

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

    def get_status(self):
        return self.status


# Child class
class Supervisor(Account):
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
    course_id = models.IntegerField()
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

    def remove_lab(self, lab):
        pass

    def display_lab(self):
        pass


class Lab(models.Model):
    lab_name = models.CharField(max_length=30)
    lab_id = models.IntegerField()
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


# for course table
class Courses(models.Model):
    name = models.CharField(max_length=300, verbose_name="course name")
