import django_tables2 as tables
from .models import Courses


class CoursesTable(tables.Table):
    class Meta:
        model = Courses
        exclude =("user",)
