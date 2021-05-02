from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from TA_Scheduler.models import Account, Instructor, Supervisor, TA, Courses
from django.contrib import messages


# Create your views here.

class HomeView(View):
    def get(self, request):
        return render(request, "home.html")


class LoginView(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        name = request.POST['name']
        password = request.POST['password']
        if name == 'user' and password == 'user':
            return render(request, "login.html", {"name": name, "password": password})
        elif name == 'admin' and password == 'admin':
            return render(request, "AdminP.html", {"name": name})
        else:
            return render(request, "login.html", {"message": "Information is incorrect"})


class CoursesView(View):

    def get(self, request):
        return render(request, "courses.html")

    def post(self, request):
        if request.method == 'POST':
            # admin - create courses and sections
            course_name = request.POST['courseName']
            course_number = request.POST['courseNumber']
            course_semester = request.POST['courseSemester']
            course = Courses.objects.create(name=course_name, cid=course_number, semester=course_semester)
            course.save()
            messages.success(request, f'The COURSE SUCCESSFULLY CREATED!')
            return redirect('/courses')
        else:
            return render(request, 'TA_Scheduler/AdminP.html')


def courses_information_view(request):
    obj = Courses.objects.get(id=1)
    #context = {
     ### 'semester': obj.semester
    #}
    context ={
        'object': obj
    }
    return render(request, "/supervisor", context)


class AdminView(View):
    def get(self, request):
        return render(request, "AdminP.html")


class New(View):
    def get(self, request):
        return render(request, 'newAccount.html')

    def post(self, request):

        # determine status
        num = int(request.POST.get('status'))
        if num == 8:
            user = Supervisor()
        elif num == 5:
            user = Instructor()
        else:
            user = TA()

        user.name = request.POST.get('first_name')
        user.lastname = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.phone_number = request.POST.get('phone')
        user.home_address = request.POST.get('address')
        user.status = request.POST.get('status')
        user.save()

        content = {
            'name': user.name,
            'lastname': user.lastname,
            'email': user.email,
            'phone_num': user.phone_number,
            'address': user.home_address,
            'status': user.status
        }

        return render(request, "AdminP.html", content)


class EmailView(View):
    def get(self, request):
        return render(request, "Email.html")


class InstructorView(View):
    def get(self, request):
        return render(request, "instructor.html")


class LabView(View):
    def get(self, request):
        return render(request, "lab.html")
