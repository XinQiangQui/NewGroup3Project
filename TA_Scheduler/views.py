from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView


# from django_tables2 import SingleTableView


# from .tables import CoursesTable


# Create your views here.

class HomeView(View):
    def get(self, request):
        return render(request, "home.html")

    def post(self, request):
        name = request.POST['name']
        password = request.POST['password']
        if name == 'user' and password == 'user':
            return render(request, "home.html", {"name": name, "password": password})
        elif name == 'admin' and password == 'admin':
            return render(request, "AdminP.html", {"name": name, "password": password})
        else:
            return render(request, "home.html", {"message": "Information is incorrect"})
