from django.contrib import admin
from .models import Account, TA, Assignment, Instructor, Supervisor, Lab, Courses #CourseSection

# Register your models here.
admin.site.register(Account)
admin.site.register(TA)
admin.site.register(Supervisor)
admin.site.register(Instructor)
admin.site.register(Assignment)
admin.site.register(Lab)
admin.site.register(Courses)
#admin.site.register(CourseSection)
