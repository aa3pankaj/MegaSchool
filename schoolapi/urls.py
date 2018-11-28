"""apisite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers
from .views import StudentView,StudentDetailView,ParentDetailView,ParentView,ParentChildView,StudentAttendanceDetailView,StudentAttendanceView

# router = routers.DefaultRouter()
# router.register(r'student',StudentViewSet,'student')
# router.register(r'parent', ParentViewSet,'parent')
# router.register(r'parent/<int:username>/child',ParentChildList.as_view(),'parentchild')
# urlpatterns = [
#
#     url(r'^profile/', include(router.urls)),
# ]
urlpatterns = [

url(r'^profile/parent/$', ParentView.as_view(),name='parent'),
url(r'^profile/student/(?P<user_id>\d+)/$', StudentDetailView.as_view(),name='studentinfo'),
url(r'^profile/parent/(?P<user_id>\d+)/$', ParentDetailView.as_view(),name='parentinfo'),
url(r'^profile/parent/(?P<user_id>\d+)/child/$', ParentChildView.as_view()),
url(r'^attendence/(?P<user_id>\d+)/$', StudentAttendanceView.as_view()),
url(r'^attendence/(?P<user_id>\d+)/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/$', StudentAttendanceDetailView.as_view()),
url(r'^attendence/add/(?P<user_id>\d+)/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/(?P<value>[\w\-]+)/$', StudentAttendanceAddView.as_view()),

]
