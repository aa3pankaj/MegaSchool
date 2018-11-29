from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import StudentSerializer, ParentSerializer,AttendanceSerializer
from .models import Student,Parent,Attendance
from rest_framework import  generics
from rest_framework.response import Response
import datetime
class StudentView(generics.ListAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

class StudentDetailView(generics.ListCreateAPIView):
    serializer_class = StudentSerializer
    def get_queryset(self):
        user_id = self.kwargs["user_id"]
        queryset = Student.objects.filter(id=user_id)
        return queryset

class ParentView(generics.ListAPIView):
    serializer_class = ParentSerializer
    queryset = Parent.objects.all()


class ParentDetailView(generics.ListCreateAPIView):
    serializer_class = ParentSerializer
    def get_queryset(self):
        user_id = self.kwargs["user_id"]
        queryset = Parent.objects.filter(id=user_id)
        return queryset


class ParentChildView(generics.ListAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self):
        user_id = self.kwargs["user_id"]

        parent = Parent.objects.get(id=user_id)
        return parent.student_set.all()
class StudentAttendanceDetailView(generics.ListCreateAPIView):
     serializer_class=AttendanceSerializer

     def get_queryset(self):
         day = self.kwargs["day"]
         month = self.kwargs["month"]
         year = self.kwargs["year"]
         user_id = self.kwargs["user_id"]
         student = Student.objects.get(id=user_id)

         date=datetime.datetime.strptime(year+'-'+month+'-'+day, '%Y-%m-%d').date()
         return student.attendance_set.filter(date=date)

class StudentAttendanceView(generics.ListAPIView):
    serializer_class = AttendanceSerializer

    def get_queryset(self):
        user_id = self.kwargs["user_id"]
        student=Student.objects.get(id=user_id)
        return student.attendance_set.all()


# class StudentAttendanceCreateView(generics.ListCreateAPIView):
#     queryset = Attendance.objects.all()
#     serializer_class = AttendanceSerializer
#
#     def create(self, request, *args, **kwargs):
#         write_serializer = AttendanceCreateSerializer(data=request.data)
#         write_serializer.is_valid(raise_exception=True)
#         instance = self.perform_create(write_serializer)
#
#         read_serializer = AttendanceSerializer(instance)
#
#         return Response(read_serializer.data)


