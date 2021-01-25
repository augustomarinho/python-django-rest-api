from django.urls import path
from rest_api.api import views

urlpatterns = [
    path('currentdate', views.DateAPI.as_view())
]
