from django.contrib import admin
from .models import Student,Parent,Attendance,Teacher,ClassRoom,Course,Subject,Exam,ExamResult,ExamType
# Register your models here.

admin.site.register(Student)
admin.site.register(Parent)
admin.site.register(Attendance)
admin.site.register(Teacher)
admin.site.register(ClassRoom)
admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(Exam)
admin.site.register(ExamResult)
admin.site.register(ExamType)


