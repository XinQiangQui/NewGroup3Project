from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

# from django_tables2 import SingleTableView

from .models import Courses


# from .tables import CoursesTable


# Create your views here.

class HomeView(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        name = request.POST['name']
        password = request.POST['password']
        return render(request, "home.html", {"name": name, "password": password})


class CoursesView(View):
    def get(self, request):
        return render(request, "courses.html")

    def courseview(request):
        all_courses_items = Courses.objects.all()

        return render(request, "courses.html", {'all_courses': all_courses_items})


def addcoursesview(request):
    x = request.Post['name']
    new_course = Courses(name=x)
    new_course.save()
    return HttpResponseRedirect('/TA_Scheduler/')
