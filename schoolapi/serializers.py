from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Student,Parent

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ('__all__')

class ParentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Parent
        fields = ('__all__')