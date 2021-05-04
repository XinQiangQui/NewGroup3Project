from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
from TA_Scheduler.models import Account

from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm


def get_all_account():
    accounts = list(Account.objects.all())
    formatted_account = []
    for i in accounts:
        tmp_account = {'name': i.name,
                       'lastname': i.lastname,
                       'email': i.email,
                       'phone_number': i.phone_number,
                       'home_address': i.home_address,
                       'password': i.password,
                       'status': i.status}
        formatted_account.append(tmp_account)
    return formatted_account


def get_account(username):
    tmp = get_all_account()

    for i in tmp:
        account_name = i.get("name")
        if account_name == username:
            return i


def log_out(request):
    del request.session
    redirect('/login')


# done
class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        name = request.POST["name"]
        password = request.POST["password"]

        tmp = get_all_account()

        for i in tmp:
            account_name = i.get("name")
            account_password = i.get("password")
            account_status = i.get("status")

            if name == account_name and password == account_password:

                if account_status == 'Supervisor':
                    return render(request, 'AdminP.html', i)
                elif account_status == 'Instructor':
                    return render(request, 'Instructor.html', i)
                else:
                    return render(request, 'TA.html', i)

        return render(request, 'login.html')


class AdminView(View):
    def get(self, request):
        return render(request, 'AdminP.html')


def edit_page(request, username):
    user = get_account(username)
    return render(request, 'edit_account.html', user)


class NewAccount(View):
    def get(self, request):
        return render(request, 'newAccount.html')

    def post(self, request):
        tmp = Account(name=request.POST["first_name"],
                      lastname=request.POST["last_name"],
                      email=request.POST["email"],
                      phone_number=request.POST["phone"],
                      home_address=request.POST["address"],
                      status=request.POST["status"])
        tmp.save()

        return render(request, 'AdminP.html')


class EditView(View):
    def get(self, request):
        return render(request, 'edit_account.html')


def ta_view(request):
    def get(self, request):
        return render(request, 'login.html')


def instructor_view(request):
    def get(self, request):
        return render(request, 'login.html')
