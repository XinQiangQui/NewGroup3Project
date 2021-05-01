from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
from TA_Scheduler.models import Account, Instructor, Supervisor, TA

from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.


class LoginView(View):
    @staticmethod
    def login(self, request):
        """
        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                username = request.POST['username']
                if username

        """
        pass

    def create_account(self, request):
        pass

    def forgot_password(self, request):
        pass


def admin_view(request):
    pass


def ta_view(request):
    pass


def instructor_view(request):
    pass

