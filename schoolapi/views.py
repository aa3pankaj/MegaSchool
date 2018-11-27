from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import StudentSerializer, ParentSerializer
from .models import Student,Parent
from rest_framework import generics

class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    # def get_queryset(self):
    #     username = self.request.query_params.get('username')
    #     queryset = Student.objects.filter(user_id=username)
    #
    #     return queryset

class ParentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer

class ParentChildList(generics.ListAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        #add changes based on current user
        #user = self.request.user
        parent = Parent.objects.get(id=self.kwargs['username'])
        return parent.student_set.all()