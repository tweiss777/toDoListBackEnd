from django.db import models
import datetime as dt

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50) 
    password = models.CharField(max_length = 50) 
    date_created = models.DateTimeField(default=dt.now)



class ToDoList(models.Model):
    list_id = models.AutoField(primary_key=True)
    list_name = models.CharField(max_length=50)
    user_id = models.ForeignKey('User',on_delete=models.CASCADE)

class ToDoItem(models.Model):
    item_name = models.CharField(max_length=50)
    list_id = models.ForeignKey('ToDoList',on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=dt.now)