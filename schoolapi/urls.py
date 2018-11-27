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
from .views import StudentViewSet,ParentViewSet,ParentChildList

# router = routers.DefaultRouter()
# router.register(r'student',StudentViewSet,'student')
# router.register(r'parent', ParentViewSet,'parent')
# router.register(r'parent/<int:username>/child',ParentChildList.as_view(),'parentchild')
# urlpatterns = [
#
#     url(r'^profile/', include(router.urls)),
# ]
urlpatterns = [
    url(r'^profile/student/', StudentViewSet),
url(r'^profile/parent/', ParentViewSet),
url(r'^profile/parent/<int:username>/child/', ParentChildList),
]
