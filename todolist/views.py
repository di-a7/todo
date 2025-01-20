from django.shortcuts import render, redirect
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
      description = request.POST.get('description')
      if title == '' and description == '':
         context = {
            "error":"Both fields are required."
         }
         return render(request,'create.html',context)
      Todolist.objects.create(Title = title, Description = description)
      return redirect('/task')
   return render(request,'create.html')

def task_mark(request,pk):
   task = Todolist.objects.get(pk = pk)
   task.status = True
   task.save()
   return redirect("/task")

def task_edit(request, pk):
   task = Todolist.objects.get(pk = pk)
   context = {"tasks":task}
   if request.method == "POST":
      title = request.POST.get('title')
      description = request.POST.get('description')
      task.Title = title
      task.Description = description
      task.save()
      return redirect('/task')
   return render(request, 'edit.html',context)
# contact, about...