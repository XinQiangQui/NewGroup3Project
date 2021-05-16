import unittest

from django.test import TestCase, Client
from .models import Account, Course, Lab, PersonalInfo


# Author : Xin Qiang


# Tests for login
class LoginTest(unittest.TestCase):
    def setUp(self):
        self.Client = Client()

        # create a tmp supervisor account
        # self.supervisor = Supervisor(name='user1', password='password')
        self.supervisor.save()

        # create a tmp instructor account
        # self.instructor = Instructor(name='user2', password='password')
        self.instructor.save()

        # create a tmp TA account
        # self.TA = TA(name='user3', password='password')
        self.TA.save()

    # test for correct name and password (supervisor)
    def testCorrectSupervisor(self):
        response = self.Client.post('/', {'username': 'user1', 'password': 'password'})
        self.assertTrue(response.url, 'Username and password are correct')

    # test for correct name and password (Instructor)
    def testCorrectInstructor(self):
        response = self.Client.post('/', {'username': 'user2', 'password': 'password'})
        self.assertTrue(response.url, 'Username and password are correct')

    # test for correct name and password (TA)
    def testCorrectTA(self):
        response = self.Client.post('/', {'username': 'user3', 'password': 'password'})
        self.assertTrue(response.url, 'Username and password are correct')

    # test for not existed name
    def test_WrongName(self):
        response = self.Client.post('/', {'username': 'wrong', 'password': 'password'})
        self.assertFalse(response.context["username"], 'Username not found')

    # test for wrong password
    def test_WrongPassword(self):
        response = self.Client.post('/', {'username': 'user1', 'password': 'wrong'})
        self.assertFalse(response.context["password"], 'Password is incorrect')

    # test for null name
    def test_NullName(self):
        response = self.Client.post('/', {'username': '', 'password': 'password'})
        self.assertFalse(response.context["username"], 'Username cannot be empty')

    # test for null password
    def test_NullPassword(self):
        response = self.Client.post('/sign in/', {'username': 'user1', 'password': ''})
        self.assertFalse(response.context["password"], 'Password cannot be empty')


# more unit tests


# test for supervisor class
class SupervisorTest(TestCase):
    pass


# test for instructor class
class InstructorTest(TestCase):
    pass


# test for TA
class TaTest(TestCase):
    pass


# Test Course Model
class TestCourse(unittest.TestCase):
    def test_name(self):
        obj = Course.objects.get(id='1')
        self.assertTrue(isinstance(obj, str), 'test_name must be a Char Field!')
        self.assertFalse(any(char.isdigit() for char in obj))
        self.assertTrue(obj.name.len() <= 20)

    def test_cId(self):
        obj = Course.objects.get(id='1')
        self.assertTrue(isinstance(obj, int), 'course Id  must be a Integer Field!')
        self.assertTrue(obj.cId.len() <= 3)

    def test_semester(self):
        obj = Course.objects.get(id='1')
        self.assertTrue(isinstance(obj, int), 'number must be a Char Field!')
        self.assertTrue(obj.semester.len() <= 20)


# Test Lab Model
class LabTest(unittest.TestCase):
    def test_course(self):
        obj = Lab.objects.get(id='1')
        self.assertFalse(obj is None, 'Foreign key for course in lab model is null!')

    def test_labId(self):
        obj = Lab.objects.get(id='1')
        self.assertTrue(isinstance(obj, int), 'Lab Id must be an Integer Field!')
        self.assertTrue(obj.number.len() <= 20, 'Lab Id  is to long!')
        self.assertFalse(obj.number.len() == 0, 'Lab Id is empty!')
        self.assertFalse(obj.number is None, 'Lab Id is null!')


# Test the personal information Update, this features has not been fully implemented
class PersonalInfoTest(unittest.TestCase):
    def test_office(self):
        obj = PersonalInfo.objects.get(id='1')
        self.assertTrue(len(obj) <= 20, 'Office is to long!')
        self.assertIsInstance(obj, int, 'Office is not right instance!')
        self.assertFalse(obj.len() == 0, 'PersonalInfo office is empty!')

    def test_email(self):
        obj = PersonalInfo.objects.get(id='1')
        self.assertIsInstance(obj, str, 'email must be a Char field.')
        self.assertTrue(len(obj) <= 20, 'email is to long!')
        self.assertFalse(obj.len() == 0, 'email is empty!')

    def test_phone_num(self):
        obj = PersonalInfo.objects.get(id='1')
        self.assertIsInstance(obj, int, 'Phone_num is not right instance!')
        self.assertFalse(obj.len() == 0, 'Section meeting_location is empty!')

    def test_office_hours(self):
        obj = PersonalInfo.objects.get(id='1')
        self.assertIsInstance(obj, str, 'Office hours must be a Char field.')
        self.assertTrue(len(obj) <= 20, 'Office hours is to long!')
        self.assertFalse(obj.len() == 0, 'Office hours is empty!')
