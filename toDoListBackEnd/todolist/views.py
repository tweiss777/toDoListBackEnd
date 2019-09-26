from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from toDoListBackEnd.todolist.models import *
from toDoListBackEnd.todolist.serializers import *
from django.views.decorators.csrf import csrf_exempt
import json 

# test route
def index(request):
    return HttpResponse("homepage of the api")
# Create your views here.

# view that lists all the to do lists 
@csrf_exempt
def retrieveToDoItems(request):
    if request.method == 'GET':
        return HttpResponse("Request invalid")
    elif request.method == 'POST':
        userId = request.POST['user_id']
        listName = request.POST['list_name']
        todolist = ToDoList.objects.get(list_name=listName,user_id=userId)
        list_serializer = ToDoListSerializer(todolist)
        return HttpResponse(json.dumps(list_serializer.data))

# create a todo list for the specified user
@csrf_exempt
def create_list(request):
    if request.method == 'GET':
        return HttpResponse("Request invalid")

    elif request.method == 'POST':
        list_name = request.POST['list_name']
        user_id = request.POST['user_id']

#create list item for the specified user's list
@csrf_exempt
def create_list_item(request):
    if request.method == 'GET':
        return HttpResponse("Request invalid")
    elif request.method == 'POST':
        pass

# edit the name of the list item
@csrf_exempt
def update_list_item(request):
    if request.method == 'GET':
        return HttpResponse("Request invalid")
    elif request.method == 'POST':
        pass

# edit the name of the list itself
@csrf_exempt
def update_list_name(request):
    if request.method == 'GET':
        return HttpResponse("Request invalid")
    elif request.method == 'POST':
        pass

#delete list itself
@csrf_exempt
def delete_list(request):
    if request.method == 'GET':
        return HttpResponse("Request invalid")
    elif request.method == 'POST':
        pass

# delete list item
@csrf_exempt
def delete_list_item(request):
    if request.method == 'GET':
        return HttpResponse("Request invalid")
    elif request.method == 'POST':
        pass