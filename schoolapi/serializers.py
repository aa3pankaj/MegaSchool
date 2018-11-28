from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Student,Parent,Attendance

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
