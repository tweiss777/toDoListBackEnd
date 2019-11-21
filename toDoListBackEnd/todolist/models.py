from django.db import models
from datetime import datetime as dt
from django.contrib.auth.models import User as u

# Create your models here.
# the user model should inherit the built-in one
class User(models.Model):
    user_id = models.AutoField(primary_key=True) 
    first_name = models.CharField(max_length = 50) # Included
    last_name = models.CharField(max_length = 50) # Included
    email = models.CharField(max_length = 50)  # Inclued
    password = models.CharField(max_length = 50) # Included
    date_created = models.DateTimeField(default=dt.now)



class ToDoList(models.Model):
    # list id will be created automatically
    list_id = models.AutoField(primary_key=True)
    list_name = models.CharField(max_length=50)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,related_name="todolists")

# make list_id the primary key
class ToDoItem(models.Model):
    item_name = models.CharField(max_length=50)
    list_id = models.ForeignKey(ToDoList,related_name="list_items",on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=dt.now)