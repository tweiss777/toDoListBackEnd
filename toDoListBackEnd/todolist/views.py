from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from toDoListBackEnd.todolist.models import *
from toDoListBackEnd.todolist.serializers import *
from django.views.decorators.csrf import csrf_exempt
import json 
from datetime import datetime as dt

# test route
def index(request):
    return HttpResponse("homepage of the api")
# Create your views here.

@csrf_exempt
def retrieveToDoLists(request):
    if request.method == 'GET':
        return HttpResponse("Request invalid")
    elif request.method == 'POST':
        userID = request.POST.get('user_id')
        try:
            todolists = ToDoList.objects.filter(user_id=userID)
            serializer = ToDoListSerializer(todolists,many=True)
            return HttpResponse(json.dumps(serializer.data))
        except :
            return HttpResponse("Something went wrong while retrieving todo lists")
    


# view that lists all the to do lists 
@csrf_exempt
def retrieveToDoItems(request):
    if request.method == 'GET':
        return HttpResponse("Request invalid")
    elif request.method == 'POST':
        userId = request.POST.get("user_id")
        listName = request.POST.get("list_name")
        todolist = ToDoList.objects.get(list_name=listName,user_id=userId)
        list_serializer = ToDoListSerializer(todolist)
        return HttpResponse(json.dumps(list_serializer.data))

# create a todo list for the specified user
@csrf_exempt
def create_list(request):
    if request.method == 'GET':
        return HttpResponse("Request invalid")

    elif request.method == 'POST':
        listName = request.POST.get('list_name')
        userId = request.POST.get('user_id')
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
        # list id
        # current item name
        current_list_item = request.POST.get('list_item')
        # item name to update with
        updated_list_item = request.POST.get('updated_list_item')
        listId = request.POST.get('list_id')
        toDoItem = ToDoItem.objects.get(list_id=listId,item_name=current_list_item)
        try:
            toDoItem.item_name = updated_list_item
            toDoItem.date_created = dt.now 
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
        listID = request.POST.get('list_id')
        userID = request.POST.get('user_id')
        new_name = request.POST.get('new_name')
        current_list = ToDoList.objects.get(list_id=listID,user_id=userID)
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
        listID = request.POST.get('list_id')
        listName = request.POST.get('list_name')
        # retrieve the list items in the form of a queryset
        try:
            list_items = ToDoItem.objects.filter(list_id=listID)
            listName = ToDoList.objects.get(list_name=listName,list_id=listID)
            if len(list_items) > 0:
                rowsDeleted = list_items.delete()
            listName.delete()
        except:
            return HttpResponse("Something went wrong while processing the delete")
        return HttpResponse("List deleted \n number of items removed from list %s" % rowsDeleted.count)
# delete list item
@csrf_exempt
def delete_list_item(request):
    if request.method == 'GET':
        return HttpResponse("Request invalid")
    elif request.method == 'POST':
        listId = request.POST.get('list_id')
        listItemToDelete = request.POST.get('list_item')
        try:
            item = ToDoItem.objects.get(list_id=listId,item_name=listItemToDelete)
            item.delete()
        except:
            return HttpResponse("Something went wrong while deleting entry")
        return HttpResponse("Item succesfully deleted")