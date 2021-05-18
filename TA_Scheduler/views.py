from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
from TA_Scheduler.models import Account, Supervisor, Instructor, TA, Course
from django.contrib import messages

from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm


def log_out(request):
    del request.session
    redirect('/login')


class LoginView(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        username = request.POST["name"]
        password = request.POST["password"]
        accounts = Account.objects.all()

        request.session["username"] = username

        for i in accounts:
            account_name = i.name
            account_password = i.password
            account_status = i.status

            if username == account_name and password == account_password:
                request.session["username"] = account_name
                if account_status == 'Supervisor':
                    return render(request, 'AdminP.html', {"accounts": accounts,
                                                           "courses": Course.objects.all(),
                                                           "name": username})
                elif account_status == 'Instructor':
                    return render(request, 'Instructor.html')
                else:
                    return render(request, 'TA.html')

        return render(request, "login.html")


class AdminView(View):
    def get(self, request):
        return render(request, 'AdminP.html', {"accounts": Account.objects.all(),
                                               "courses": Course.objects.all(),
                                               "name": request.session.get("username")})


def edit_page(request):
    if request.session.get("username"):
        return render(request, 'edit_account.html')
    return render(request, "Login.html")


class NewAccount(View):
    def get(self, request):
        if request.session.get("username"):
            return render(request, 'newAccount.html')
        return render(request, 'Login.html')

    def post(self, request):
        # create account
        tmp = Account.objects.create(name=request.POST["first_name"],
                                     lastname=request.POST["last_name"],
                                     email=request.POST["email"],
                                     phone_number=request.POST["phone"],
                                     home_address=request.POST["address"],
                                     password=request.POST["password"],
                                     status=request.POST["status"])

        return render(request, 'AdminP.html', {"accounts": Account.objects.all(),
                                               "courses": Course.objects.all(),
                                               "username": request.session.get("username")})


class CoursesView(View):
    def get(self, request):
        if request.session.get("username"):
            return render(request, 'courses.html')
        return render(request, "Login.html")

    def post(self, request):
        course = Course.objects.create(name=request.POST["course_name"],
                                       cId=request.POST["course_ID"],
                                       semester=request.POST["semester"])

        messages.success(request, 'COURSE SUCCESSFULLY CREATED')
        return render(request, 'AdminP.html', {"accounts": Account.objects.all(),
                                               "courses": Course.objects.all(),
                                               "username": request.session.get("username")})


# not yet implemented
class EditView(View):
    def get(self, request):
        if request.session.get("username"):
            return render(request, 'edit_account.html')
        return render(request, "Login.html")

    def post(self, request):
        pass


class InstructorToCourse(View):
    def get(self, request):
        if request.session.get("username"):
            accounts = Account.objects.filter(status='Instructor').all()
            return render(request, 'instructor_to_course.html', {"accounts": accounts,
                                                                 "courses": Course.objects.all()})
        return render(request, 'Login.html')

    def post(self, request):
        instructor_name = request.POST["instructor_name"]
        course_id = request.POST["course_id"]
        instructor = Account.objects.filter(name=instructor_name)
        course = Course.objects.filter(cId=course_id)
        course.instructor = instructor

        return render(request, 'AdminP.html', {"accounts": Account.objects.all(),
                                               "courses": Course.objects.all(),
                                               "username": request.session.get("username")})

class TaToCourse(View):
    def get(self, request):
        return render(request, 'ta_to_lab.html')

    class CoursesView(View):
        def get(self, request):
            if request.session.get("username"):
                return render(request, 'courses.html')
            return render(request, "Login.html")

        def post(self, request):
            course = Course.objects.create(name=request.POST["course_name"],
                                           cId=request.POST["course_ID"],
                                           semester=request.POST["semester"])

            messages.success(request, 'COURSE SUCCESSFULLY CREATED')
            return render(request, 'AdminP.html', {"accounts": Account.objects.all(),
                                                   "courses": Course.objects.all(),
                                                   "username": request.session.get("username")})


def ta_view(request):
    def get(self, request):
        return render(request, 'login.html')


def instructor_view(request):
    def get(self, request):
        return render(request, 'login.html')

class ManageAsView(View):
    def get(self, request):
        if request.session.get("username"):
            return render(request, 'courses.html')
        return render(request, "Login.html")

    def post(self, request):
        course = Course.objects.create(name=request.POST["ass_name"],
                                       startDate=request.POST["start"],
                                       endDate=request.POST["end"])

        messages.success(request, 'Assignment Created')
        return render(request, 'AdminP.html', {"accounts": Assignment.objects.all()})
