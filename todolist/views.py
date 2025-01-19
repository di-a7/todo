from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import *
# Create your views here.
def home(request):
   person = [
   {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 60},
    {"name": "Charlie", "age": 22},
    {"name": "Diana", "age": 58},
    {"name": "Ethan", "age": 35},
   ]
   context = {
      'name':"Home Page",
      'persons': person       }
   return render(request,'home.html',context)

def index(request):
   return HttpResponse("This is index function.")

def contact(request):
   return render(request, 'contact.html')

def task_list(request):
   tasks = Todolist.objects.all()
   context = {
      "tasks":tasks
   }
   return render(request, 'task.html',context)

def task_create(request):
   if request.method == "POST":
      title = request.POST.get('title')
      return HttpResponse(title)
   return render(request,'create.html')
# contact, about...