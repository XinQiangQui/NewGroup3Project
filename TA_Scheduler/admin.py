from django.contrib import admin
from .models import Account, Assignment, Lab, Course, PersonalInfo, Skill #TA, Supervisor, Instructor

# Register your models here.
admin.site.register(Account)
#admin.site.register(TA)
#admin.site.register(Supervisor)
#admin.site.register(Instructor)
admin.site.register(Assignment)
admin.site.register(Lab)
admin.site.register(Course)
admin.site.register(PersonalInfo)
admin.site.register(Skill)
