from django.db import models
from datetime import datetime as dt

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
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)

# make list_id the primary key
class ToDoItem(models.Model):
    item_name = models.CharField(max_length=50)
    list_id = models.ForeignKey(ToDoList,related_name="list_items",on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=dt.now)