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

        return render(request, "courses.html", {'all_courses': all_courses_items})


def addcoursesview(request):

#    x = request.Post['name']
 #   new_course = Courses(name=x)
  #  new_course.save()

    return HttpResponseRedirect('/TA_Scheduler/')



def logout(self, request):
    return render(request, "login.html")

class New(View):
    def get(self, request):
        return render(request, 'newAccount.html')
