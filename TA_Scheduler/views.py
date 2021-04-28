from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
from TA_Scheduler.models import Account, Instructor, Supervisor, TA


# Create your views here.

class HomeView(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        name = request.POST['name']
        password = request.POST['password']
        if name=='user' and password=='user':
            return render(request, "home.html", {"name": name, "password": password})
        elif name=='admin' and password=='admin':
            return render(request, "AdminP.html", {"name": name})
        else:
            return render(request, "login.html", {"message": "Information is incorrect"})

class CoursesView(View):
    def get(self, request):
        return render(request, "courses.html")

  #  def courseview(request):
#        all_courses_items = Courses.objects.all()

  #      return render(request, "courses.html", {'all_courses': all_courses_items})


class AdminView(View):
    def get(self, request):
        return render(request, "AdminP.html")

class New(View):
    def get(self, request):
        return render(request, 'newAccount.html')

    def post(self, request):
        name = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        phone_number = request.POST['phone']
        address = request.POST['address']
        password = request.POST['password']
        status = request.POST['status']

        tmp_user = None
        if status == 'Supervisor':
            tmp_user = Supervisor.supervisor(name, lastname, email, phone_number, address, password)
        elif status == 'Instructor':
            tmp_user = Instructor.instructor(name, lastname, email, phone_number, address, password)
        else:
            tmp_user = TA.ta(name, lastname, email, phone_number, address, password)

        return render(request, "AdminP.html", {"user": tmp_user})
