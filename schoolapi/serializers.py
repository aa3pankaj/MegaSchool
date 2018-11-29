from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Student,Parent,Attendance,Teacher,Exam

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('__all__')

class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = ('__all__')

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ('__all__')

class AttendanceCreateSerializer(serializers.ModelSerializer):
    student=StudentSerializer
    class Meta:
        model = Attendance
        fields = ('id', 'date', 'status','student')

    # def create(self, validated_data):
    #     #user_id = validated_data.pop('user_id')
    #     student=validated_data.pop('student')
    #     date = validated_data.pop('date')
    #     status = validated_data.pop('status')
    #     stdObj=Student.objects.get(id=student)
    #     #student=Student.objects.get(id=user_id)
    #     #instance = Attendance.objects.create(**validated_data)
    #     instance=Attendance(date=date,status=status)
    #     instance['student']=stdObj
    #     #instance.student.add(student)
    #
    #     return instance
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('__all__')


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ('__all__')