# from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
   path('home/',home),
   path('index/',index),
   path('contact/',contact),
   path('task/',task_list),
   path('task/create/',task_create),
   path('task/<pk>/',task_mark),
   path('task/<pk>/edit/',task_edit),
]