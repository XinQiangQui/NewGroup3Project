from django.shortcuts import render, redirect
from django.views import View
from TA_Scheduler.models import Account, Course, PersonalInfo, Lab
from django.contrib import messages, auth
from django.contrib.auth import authenticate

from django.contrib.auth import login


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
        request.session["password"] = password
        user = auth.authenticate(username=username, password=password)
        for i in accounts:
            account_name = i.name
            account_password = i.password
            account_status = i.status

            if username == account_name and password == account_password:
                request.session["username"] = account_name
                request.session["password"] = account_name
                if account_status == 'Supervisor':
                    return render(request, 'AdminP.html', {"accounts": accounts,
                                                           "courses": Course.objects.all(),
                                                           "name": username})
                elif account_status == 'Instructor':
                    return render(request, 'Instructor.html')
                else:
                    return render(request, 'TA.html')
            else:
                messages.info(request, 'Incorrect Username / Password')
                return render(request, "login.html")
        return render(request, "login.html")


class AdminView(View):
    def get(self, request):
        return render(request, 'AdminP.html', {"accounts": Account.objects.all(),
                                               "courses": Course.objects.all(),
                                               "name": request.session.get("username")})


class delete_account(View):
    def get(self, request):
        return render(request, 'delete_account.html', {"accounts": Account.objects.all(),
                                                       "name": request.session.get("username")})

    def post(self, request):
        name = request.POST['name']
        Account.objects.filter(name=name).delete()
        course = Course.objects.filter(instructor_name=name)
        print(course)
        course.instructor_name = ""
        print(course.instructor_name)
        return render(request, 'delete_account.html', {"accounts": Account.objects.all(),
                                                       "courses": Course.objects.all(),
                                                       "name": request.session.get("username")})

class delete_course(View):
    def get(self, request):
        return render(request, 'delete_course.html', {"courses": Course.objects.all(),
                                                      "name": request.session.get("username")})

    def post(self, request):
        name = request.POST['name']
        course = Course.objects.filter(name=name)
        print(123)
        course.delete()
        print(1234)
        return render(request, 'delete_course.html', {"courses": Course.objects.all(),
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
            accounts = Account.objects.filter(status='Instructor')
            return render(request, 'instructor_to_course.html', {"accounts": accounts,
                                                                 "courses": Course.objects.all()})
        return render(request, 'Login.html')

    def post(self, request):
        instructor_name = request.POST["instructor_name"]
        course_name = request.POST["course_name"]
        course = Course.objects.filter(name=course_name)
        course.update(instructor_name=instructor_name)

        return render(request, 'AdminP.html', {"accounts": Account.objects.all(),
                                               "courses": Course.objects.all(),
                                               "username": request.session.get("username")})


class TaToCourse(View):
    def get(self, request):
        return render(request, 'ta_to_lab.html')


def ta_view(request):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        return render(request, 'ta_page.html')


def instructor_view(request):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        return render(request, 'instructor.html')


# personal info for instructor
def Personal_Info_Instructor(request):
    if request.method == 'GET':
        try:
            user_obj = PersonalInfo.objects.get(instructorOrTa=request.user)
        except PersonalInfo.DoesNotExist:
            dne = True
            messages.success(request, 'NO PERSONAL INFO FOUND')
            return render(request, 'edit_account.html', {'dne': dne})
        else:
            dne = False
            return render(request, 'edit_account.html', {'user_obj': user_obj, 'dne': dne})

    if request.method == 'POST':
        office = request.POST['office']
        phone_num = request.POST['phone_num']
        office_hours = request.POST['office_hours']
        email = request.POST['email']
        try:
            user_obj = PersonalInfo.objects.get(instructorOrTa=request.user)
        except PersonalInfo.DoesNotExist:
            PersonalInfo.objects.create(
                instructorOrTa=request.user,
                office=office,
                phone_num=phone_num,
                office_hours=office_hours,
                email=email)
            messages.success(request, 'PERSONAL INFO CREATED')
            return redirect('Personal_Info_Instructor')
        else:
            user_obj.office = office
            user_obj.phone_num = phone_num
            user_obj.office_hours = office_hours
            user_obj.email = email
            messages.success(request, 'PERSONAL INFO UPDATED')
            return redirect('Personal_Info_Instructor')


# creating lab sections for the courses
class LabsView(View):
    def get(self, request):
        if request.session.get("username"):
            return render(request, 'lab.html')
        return render(request, "Login.html")

    def post(self, request):
        lab = Lab.objects.create(lab_name=request.POST["lab_name"],
                                 lab_id=request.POST["lab_ID"],
                                 course=request.POST["course"])

        messages.success(request, 'Lab has been Created')
        return render(request, 'Instructor.html', {"accounts": Account.objects.all(),
                                                   "lab": Lab.objects.all(),
                                                   "username": request.session.get("username")})
