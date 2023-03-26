"""WhichPN URL Configuration"""
from django.urls import path
import views

urlpatterns = [
    path('', views.FindPhone.as_view(), name='index'),
    path('phone', views.endpoint, name='endpoint')
]
