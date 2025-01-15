from django.db import models

# Create your models here.
class Todolist(models.Model):
   Title = models.CharField(max_length = 10)
   Description = models.TextField()
   status = models.BooleanField(default = False)
   created_at = models.DateTimeField(auto_now_add=True)