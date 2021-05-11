"""NewGroup3Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from TA_Scheduler import views
from django.conf.urls import url
from TA_Scheduler.views import AdminView, LoginView, NewAccount, \
                                CoursesView, log_out, edit_page, InstructorToCourse, TaToCourse

urlpatterns = [

    path("admin/", admin.site.urls),
    path('', LoginView.as_view(), name='login'),
    path('supervisor/', AdminView.as_view(), name='supervisor'),
    # url(r'^supervisor/(?P<username>[a-zA-Z0-9]+)'), AdminView.as_view(), name='supervisor'),
    # url(r'^instructor/(?P<username>[a-zA-Z0-9]+)'), InstructorView.as_view(), name='instructor'),
    # url(r'^ta/(?P<username>[a-zA-Z0-9]+)'), TaView.as_view(), name='ta'),
    path('edit_page/', edit_page, name='edit'),
    path('assign_instructor_to_course/', InstructorToCourse.as_view(), name='assign_to_course'),
    path('assign_ta_to_lab/', TaToCourse.as_view(), name='assign_to_lab'),
    path('newAccount/', NewAccount.as_view()),
    path('courses/', CoursesView.as_view()),
    path('logout/', log_out, name="logout"),
    path('Instructors/', views.Personal_Info_Instructor, name='Personal_Info_Instructor')

]
