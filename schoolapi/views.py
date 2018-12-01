from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import StudentSerializer, ParentSerializer,\
    AttendanceSerializer,AttendanceCreateSerializer,\
    TeacherSerializer,ExamSerializer,UserSerializer
from .models import Student,Parent,Attendance,Teacher,Exam,Subject,CustomUser
from rest_framework import  generics,status,views
from rest_framework.response import Response
from django.http import HttpResponse
import datetime
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.contrib.auth import authenticate,logout,login
from rest_framework.permissions import AllowAny
from django.http import HttpResponseRedirect

class LoginView(views.APIView):
    permission_classes = (AllowAny,)
    authentication_classes = ()
    #serializer_class = UserSerializer
    def post(self, request, format=None):
        data = request.data

        username = data.get('username', None)
        password = data.get('password', None)

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                #return HttpResponseRedirect('/profile/student/')
                return Response(status=status.HTTP_200_OK)
                #return HttpResponse("You're logged in.")
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
class UserList(views.APIView):
    #queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
            #return HttpResponseRedirect('/profile/student/')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentView(generics.ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = StudentSerializer
    queryset = Student.objects.all()


class StudentDetailView(generics.ListCreateAPIView):
    serializer_class = StudentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    def get_queryset(self):
        #user_id = self.kwargs["user_id"]
        queryset = Student.objects.filter(user=self.request.user)
        return queryset

class ParentView(generics.ListAPIView):
    serializer_class = ParentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Parent.objects.all()


class ParentDetailView(generics.ListCreateAPIView):
    serializer_class = ParentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    def get_queryset(self):
        #user_id = self.kwargs["user_id"]
        queryset = Parent.objects.filter(user=self.request.user)
        return queryset


class ParentChildView(generics.ListAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self):
        #user_id = self.kwargs["user_id"]

        parent = Parent.objects.get(id=self.request.user)
        return parent.student_set.all()


# class StudentAttendanceCreateView(generics.ListCreateAPIView):
#     #permission_classes = (IsAuthenticatedOrReadOnly,)
#     serializer_class = AttendanceCreateSerializer
#     queryset = Attendance.objects.all()
#     def create(self, request, *args, **kwargs):
#         # day = request.POST.get("day")
#         # month = request.POST.get("month")
#         # year = request.POST.get("year")
#         # user_id = request.POST.get("student")
#         day = self.kwargs["day"]
#         month = self.kwargs["month"]
#         year = self.kwargs["year"]
#         #user_id = self.kwargs["user_id"]
#         student = Student.objects.get(user=request.user)
#         status = request.POST.get("status")
#         date = datetime.datetime.strptime(year + '-' + month + '-' + day, '%Y-%m-%d').date()
#         #instance = Attendance(date=date, student=student, status=status)
#         u = Attendance.objects.create(date=date, student=student, status=status)
#         u.save()
#
#         return HttpResponse(status=204)

class StudentAttendanceDetailView(generics.ListCreateAPIView):
     permission_classes = (IsAuthenticatedOrReadOnly,)
     serializer_class=AttendanceSerializer

     def get_queryset(self):

         day = self.kwargs["day"]
         month = self.kwargs["month"]
         year = self.kwargs["year"]
         #user_id = self.kwargs["user_id"]
         #student = Student.objects.get(id=user_id)
         student = Student.objects.get(user=self.request.user)
         date=datetime.datetime.strptime(year+'-'+month+'-'+day, '%Y-%m-%d').date()
         return student.attendance_set.filter(date=date)

     def create(self, request, *args, **kwargs):
         day = self.kwargs["day"]
         month = self.kwargs["month"]
         year = self.kwargs["year"]
         #user_id = self.kwargs["user_id"]
         student = Student.objects.get(user=self.request.user)
         status = request.POST.get("status")
         date = datetime.datetime.strptime(year + '-' + month + '-' + day, '%Y-%m-%d').date()
         #instance = Attendance(date=date, student=student, status=status)
         u = Attendance.objects.create(date=date, student=student, status=status)
         u.save()
         return HttpResponse(status=204)

class StudentAttendanceView(generics.ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = AttendanceSerializer

    def get_queryset(self):
        #user_id = self.kwargs["user_id"]
        student = Student.objects.get(user=self.request.user)
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

class TeacherView(generics.ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()


class TeacherDetailView(generics.ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = TeacherSerializer
    def get_queryset(self):
        #user_id = self.kwargs["user_id"]
        queryset = Teacher.objects.filter(user=self.request.user)
        return queryset

class ExamView(generics.ListAPIView):
    serializer_class = ExamSerializer
    queryset = Exam.objects.all()

class ExamDetailView(generics.ListAPIView):
    serializer_class = ExamSerializer

    def get_queryset(self):
        pk = self.kwargs["pk"]
        queryset = Exam.objects.filter(id=pk)
        return queryset
class SubjectExamView(generics.ListAPIView):
    serializer_class = ExamSerializer

    def get_queryset(self):
        pk = self.kwargs["pk"]
        subject = Subject.objects.get(id=pk)
        queryset = subject.exam_set.all()
        return queryset