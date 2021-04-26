from django.shortcuts import render
from django.views import View


# Create your views here.

class HomeView(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        name = request.POST['name']
        password = request.POST['password']
        return render(request, "home.html", {"name": name, "password": password})

