from django.contrib import admin
from .models import Todolist
# Register your models here.
@admin.register(Todolist)
class TodolistAdmin(admin.ModelAdmin):
   list_display = ['Title','Description','status']
   list_filter = ['status']
   list_per_page = 5
   list_editable = ['status','Description']
   search_fields = ['Title']