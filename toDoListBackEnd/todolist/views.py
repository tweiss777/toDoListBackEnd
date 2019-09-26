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
        listName = request.POST['list_name']
        userId = request.POST['user_id']
        new_list = ToDoList(list_name=listName,user_id=userId)
        try:
            new_list.save()
        except:
            return HttpResponse("Something went wrong while saving your query")
        return HttpResponse("list created succesfully")

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
        # get post params such as list_id and list_item
        # current item name
        current_list_item = request.POST['list_item']
        # item name to update with
        updated_list_item = request.POST['updated_list_item']
        listId = request.POST['list_item']
        toDoItem = ToDoItem.objects.get(list_id=listId,item_name=current_list_item)
        try:
            toDoItem.item_name = updated_list_item
            toDoItem.save()
        except:
            return HttpResponse("Something went wrong while updating to do list item")
        return HttpResponse("list item updated successfully")


# edit the name of the list itself
@csrf_exempt
def update_list_name(request):
    if request.method == 'GET':
        return HttpResponse("Request invalid")
    elif request.method == 'POST':
        userID = request.POST['user_id']
        new_name = request.POST['list_name']
        current_name = request.POST['current_list_name']
        current_list = ToDoList.objects.get(list_name=current_name,user_id=userID)
        try:
            current_list.list_name = new_name
            current_list.save()
        except:
            return HttpResponse("Something went wrong while updating")
        return HttpResponse("list name update succesfully")

#delete list itself
@csrf_exempt
def delete_list(request):
    if request.method == 'GET':
        return HttpResponse("Request invalid")
    elif request.method == 'POST':
        # if list has items then remove them
        pass

# delete list item
@csrf_exempt
def delete_list_item(request):
    if request.method == 'GET':
        return HttpResponse("Request invalid")
    elif request.method == 'POST':
        pass