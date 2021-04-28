from django.test import TestCase, Client
from .models import Supervisor, Instructor, TA

# Author : Xin Qiang


# Tests for login
class LoginTest(TestCase):
    def setUp(self):
        self.Client = Client()

        # create a tmp supervisor account
        self.supervisor = Supervisor(name='user1', password='password')
        self.supervisor.save()

        # create a tmp instructor account
        self.instructor = Instructor(name='user2', password='password')
        self.instructor.save()

        # create a tmp TA account
        self.TA = TA(name='user3', password='password')
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

