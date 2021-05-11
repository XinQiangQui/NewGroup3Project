from django.contrib import admin
from .models import Account, Assignment, Course, PersonalInfo #TA, Supervisor, Instructor

# Register your models here.
admin.site.register(Account)
#admin.site.register(TA)
#admin.site.register(Supervisor)
#admin.site.register(Instructor)
admin.site.register(Assignment)
admin.site.register(Course)
admin.site.register(PersonalInfo)
