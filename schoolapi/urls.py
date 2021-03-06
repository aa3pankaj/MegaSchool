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
from .views import StudentView,StudentDetailView,ParentDetailView,\
    ParentView,ParentChildView,StudentAttendanceDetailView,\
    StudentAttendanceView,TeacherView,\
    TeacherDetailView,ExamView,ExamDetailView,SubjectExamView,UserList,LoginView
# router = routers.DefaultRouter()
# router.register(r'student',StudentViewSet,'student')
# router.register(r'parent', ParentViewSet,'parent')
# router.register(r'parent/<int:username>/child',ParentChildList.as_view(),'parentchild')
# urlpatterns = [
#
#     url(r'^profile/', include(router.urls)),
# ]
urlpatterns = [
url(r'^profile/all/teacher/$',TeacherView.as_view(),name='teacher'),
url(r'^profile/teacher/$',TeacherDetailView.as_view(),name='teacher-info'),

url(r'^profile/all/student/$', StudentView.as_view(),name='student'),
url(r'^profile/student/$', StudentDetailView.as_view(),name='student-info'),
url(r'^attendance/$', StudentAttendanceView.as_view(),name='attendance'),
url(r'^attendance/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/$', StudentAttendanceDetailView.as_view()),
#url(r'^attendance/add/(?P<user_id>\d+)/(r'^rest-auth/registration/', include('rest_auth.registration.urls')?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/$', StudentAttendanceCreateView.as_view()),
url(r'^exam/$',ExamView.as_view(),name='exam'),
url(r'^exam/(?P<pk>\d+)/$',ExamDetailView.as_view(),name='exam-info'),
url(r'^exam/subject/(?P<pk>\d+)/$',SubjectExamView.as_view(),name='subject-exam'),

url(r'^profile/all/parent/$', ParentView.as_view(),name='parent'),
url(r'^profile/parent/$', ParentDetailView.as_view(),name='parent-info'),
url(r'^profile/parent/child/$', ParentChildView.as_view(),name='parent-child'),
url(r'^signup/$',UserList.as_view()),
    url(r'^login/$',LoginView.as_view()),
    url(r'^rest-auth/', include('rest_auth.urls')),
   # url(r'^rest-auth/registration/', include('rest_auth.registration.urls'))
]
