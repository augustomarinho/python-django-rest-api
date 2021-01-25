"""python_django_study URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include

import rest_api.api.urls
from rest_api.views import PeopleViewSet, TraininsViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('people', PeopleViewSet, basename="People")
router.register('trainings', TraininsViewSet, basename="Trainings")

urlpatterns = [
    path('', include('rest_api.urls')),
    path('api/', include(rest_api.api.urls)),
    path('crud/', include(router.urls)),
    path('admin/', admin.site.urls),
]
