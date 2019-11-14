from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from toDoListBackEnd.todolist.models import *
from toDoListBackEnd.todolist.serializers import *
from django.views.decorators.csrf import csrf_exempt
import json 
from datetime import datetime as dt
import re as regex
from toDoListBackEnd.todolist.forms import *
# test route
def index(request):
    return HttpResponse("homepage of the api")
# Create your views here.

""" Each view function checks if the request to the endpoint is a GET
    or a POST request.. 

        if the request to an endpoint is GET, then the view will return 
        an HTTPResponse with an invalid request message.

        if its a post request then the view will perform some action
    
"""

@csrf_exempt
def retrieveToDoLists(request):
    if request.method == 'GET':
        return HttpResponse("Request invalid")
    elif request.method == 'POST':
        # user_id: user id associated
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
        """Params being passed
            1) user_id = the user id that corresponds to the user
            2) list_name - which is the list name that belongs to the user
            3) In a future commit - the list id maybe required in the request to the endpoint
        
         """

        userId = request.POST.get("user_id")
        listName = request.POST.get("list_name")
        todolist = ToDoList.objects.get(list_name=listName,user_id=userId)
        list_serializer = ToDoListSerializer(todolist)
        return HttpResponse(json.dumps(list_serializer.data))

# create a todo list for the specified user
@csrf_exempt
def create_list(request):
    """
        params being passed to the post request:
            1) list_name: the name of the to do list
            2) user_id: the user id associated.
    """
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
    """
        params being passed to post request:
            1) list_id: the list id associated with the item
            2) item_name: the name of the item associated with the to do list

    """
    if request.method == 'GET':
        return HttpResponse("Request invalid")
    elif request.method == 'POST':
        listId = request.POST.get('list_id')
        new_item = request.POST.get('item_name')
        current_list = ToDoList.objects.get(list_id=listId)
        new_item = ToDoItem(list_name=new_item,list_id=current_list)
        try:
            new_item.save()
        except:
            return HttpResponse("Something went wrong while creating list item")
        return HttpResponse("Added list item")
# edit the name of the list item
@csrf_exempt
def update_list_item(request):
    if request.method == 'GET':
        return HttpResponse("Request invalid")
    elif request.method == 'POST':
        # get post params such as list_id and list_item
        # list_id: list id
        # list_item: current item name
        # list_id: the list id associated
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

# Create Account
@csrf_exempt
def create_account(request):
    print("recieved something")
   # regex for email
    regex_patten = "^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$"

    # regex_email = regex.compile(regex_patten)
    # using a form instead

    """
        url params:
            1) firts_name: the users first name
            2) last_name: the users last name
            3) email: the users email address
            4) password: the password
    """

    new_account_form = NewUserForm(request.POST)

    if new_account_form.is_valid():

        # store fields in separate variables
        firstName_field = new_account_form.cleaned_data["first_name"]
        lastName_field = new_account_form.cleaned_data["last_name"]
        email_field = new_account_form.cleaned_data["email"]
        password_field = new_account_form.cleaned_data["password"]

        new_account_model = User(first_name=firstName_field,last_name=lastName_field,email=email_field,password=password_field)
        new_account_model.save()
        return HttpResponse("Model created succesffuly \n check the database just in case")


    else:
        return HttpResponse("Error: one or more fields are invalid")

    #if form is valid
    #store entry from form in the database
    #otherwise RETURN errors


# Login
@csrf_exempt
def login(request):
    pass

@csrf_exempt
def logout(request):
    pass
    