from django.shortcuts import render
from django.views import View
from django.views.generic import ListView


# from django_tables2 import SingleTableView

# from .models import Courses
# from .tables import CoursesTable


# Create your views here.

class HomeView(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        name = request.POST['name']
        password = request.POST['password']
        return render(request, "home.html", {"name": name, "password": password})

    # table = CoursesTable(Courses.objects.all())

    #    "table":table
    # })


class CoursesView(View):
    def get(self, request):
        return render(request, "courses.html")

    # def post(self, request):
