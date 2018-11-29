#from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Student,Parent,Attendance,Teacher,Exam,CustomUser
from django.contrib.auth.models import Group

from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    #profile = StudentSerializer(required=True)
    class Meta:
        model = CustomUser
        fields = ('__all__')
    def create(self, validated_data):

        # create user
        #User = get_user_model()
        # user = CustomUser.objects.create(
        #     username=validated_data['username'],
        #     email  = validated_data['email'],
        #     user_type=validated_data['user_type']
        # )
        user=CustomUser(username=validated_data['username'],
            email  = validated_data['email'],
            user_type=validated_data['user_type'])

        user.set_password(validated_data['password'])
        user.save()
        user_type = validated_data['user_type']
        my_group = Group.objects.get(name='student')
        my_group.user_set.add(user)


        # create profile
        if user_type=='1':

            studentGroup = Group.objects.get(name='student')
            studentGroup.user_set.add(user)

            #parent_id=validated_data['parent_id']
            #parent=Parent.objects.get(parent_id)
            student = Student.objects.create(user=user,fname = validated_data['first_name'],
                                             lname = validated_data['last_name'],
            )
        elif user_type=='2':
            teacherGroup = Group.objects.get(name='teacher')
            teacherGroup.user_set.add(user)

            parent = Teacher.objects.create(user=user, fname=validated_data['first_name'],
                                           lname=validated_data['last_name'],
                                           )
        elif user_type=='3':
            parentGroup = Group.objects.get(name='parent')
            parentGroup.user_set.add(user)

            parent = Parent.objects.create(user=user, fname=validated_data['first_name'],
                                             lname=validated_data['last_name'],
                                             )
        return user
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