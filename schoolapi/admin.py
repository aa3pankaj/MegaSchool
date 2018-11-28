from django.contrib import admin
from .models import Student,Parent,Attendance,Teacher
# Register your models here.

admin.site.register(Student)
admin.site.register(Parent)
admin.site.register(Attendance)
admin.site.register(Teacher)