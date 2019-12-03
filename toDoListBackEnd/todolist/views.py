from django.shortcuts import render
from toDoListBackEnd.todolist.models import *
from toDoListBackEnd.todolist.serializers import *
from django.views.decorators.csrf import csrf_exempt
import json 
from datetime import datetime as dt
import re as regex
from toDoListBackEnd.todolist.forms import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings
from rest_framework import permissions, status
from django.contrib.auth import authenticate,login
# Create your views here.

""" Each view function checks if the request to the endpoint is a GET
    or a POST request.. 

        if the request to an endpoint is GET, then the view will return 
        an Response  with an invalid request message.

        if its a post request then the view will perform some action
    
"""

# Get the JWT settings, 
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


@csrf_exempt
@api_view(['POST'])
# Delete this method since we have the login function to handle retrieving lists
def retrieveToDoLists(request):
    if request.method == 'POST':
        # user_id: user id associated
        userID = request.data.get('user_id',None)
        todolists = ToDoList.objects.filter(user_id=userID)
        serializer = ToDoListSerializer(todolists,many=True)
        return Response(serializer.data)
    


# view that lists all the to do lists 
@csrf_exempt
@api_view(['POST'])
def retrieveToDoItems(request):
    if request.method == 'POST':
        """Params being passed
            1) user_id = the user id that corresponds to the user
            2) list_name - which is the list name that belongs to the user
            3) In a future commit - the list id maybe required in the request to the endpoint
        
         """

        userId = request.data.get("user_id")
        listName = request.data.get("list_name")
        todolist = ToDoList.objects.get(list_name=listName,user_id=userId)
        list_serializer = ToDoListSerializer(todolist)
        return Response(list_serializer.data)

# create a todo list for the specified user
@csrf_exempt
@api_view(['POST'])
def create_list(request):
    """
        params being passed to the post request:
            1) list_name: the name of the to do list
            2) user_id: the user id associated.
    """
    if request.method == 'POST':
        listName = request.data.get('list_name')
        userId = request.data.get('user_id')
        user = User.objects.get(user_id=userId)
        new_list = ToDoList(list_name=listName,user_id=user)
        new_list.save()
        return Response({"message":"list created succesfully"})

#create list item for the specified user's list
@csrf_exempt
@api_view(['POST'])
def create_list_item(request):
    """
        params being passed to post request:
            1) list_id: the list id associated with the item
            2) item_name: the name of the item associated with the to do list

    """
    if request.method == 'POST':
        listId = request.data.get('list_id')
        new_item = request.data.get('item_name')
        current_list = ToDoList.objects.get(list_id=listId)
        new_item = ToDoItem(list_name=new_item,list_id=current_list)
        new_item.save()
        Response({"message":"Added list item"})
# edit the name of the list item
@csrf_exempt
@api_view(['POST'])
def update_list_item(request):
   
    if request.method == 'POST':
        # get post params such as list_id and list_item
        # list_id: list id
        # list_item: current item name
        # list_id: the list id associated
        current_list_item = request.data.get('list_item')
        # item name to update with
        updated_list_item = request.data.get('updated_list_item')
        listId = request.data.get('list_id')
        toDoItem = ToDoItem.objects.get(list_id=listId,item_name=current_list_item)
        toDoItem.item_name = updated_list_item
        toDoItem.date_created = dt.now 
        toDoItem.save()
        Response({"message":"list item updated!"})



# edit the name of the list itself
@csrf_exempt
@api_view(['POST'])
def update_list_name(request):
    if request.method == 'POST':
        listID = request.data.get('list_id')
        userID = request.data.get('user_id')
        new_name = request.data.get('new_name')
        current_list = ToDoList.objects.get(list_id=listID,user_id=userID)
        current_list.list_name = new_name
        current_list.save()
        Response({"message":"list item updated"})


#delete list itself
@csrf_exempt
@api_view(['POST'])
def delete_list(request):
    if request.method == 'POST':
        # if list has items then remove them
        listID = request.data.get('list_id')
        listName = request.data.get('list_name')
        # retrieve the list items in the form of a queryset
        list_items = ToDoItem.objects.filter(list_id=listID)
        listName = ToDoList.objects.get(list_name=listName,list_id=listID)
        rowsToDelete = len(list_items)
        if rowsToDelete > 0:
            list_items.delete()
        listName.delete()
        return Response({"message":"List deleted \n number of items removed from list %s" % rowsToDelete})
# delete list item
@csrf_exempt
@api_view(['POST'])
def delete_list_item(request):
    if request.method == 'POST':
        listId = request.data.get('list_id')
        listItemToDelete = request.data.get('list_item')
        item = ToDoItem.objects.get(list_id=listId,item_name=listItemToDelete)
        item.delete()
        return Response({"message":"Item succesfully deleted"})

# Create Account
@api_view(['POST'])
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
    if request.method == 'POST':

        new_account_form = NewUserForm(request.data)

        if new_account_form.is_valid():

            # store fields in separate variables
            firstName_field = new_account_form.cleaned_data["first_name"]
            lastName_field = new_account_form.cleaned_data["last_name"]
            email_field = new_account_form.cleaned_data["email"]
            password_field = new_account_form.cleaned_data["password"]

            new_account_model = User(first_name=firstName_field,last_name=lastName_field,email=email_field,password=password_field)
            new_account_model.save()
            return Response({"message":"Account created succesffuly \n check the database just in case"})


        else:
            return Response({"error":"Error: one or more fields are invalid"})

        #if form is valid
        #store entry from form in the database
        #otherwise RETURN errors


@api_view(['POST'])# Login
@csrf_exempt
def login_user(request):
    
    if request.method == "POST":
        # retrieve email and password params
        email = request.data.get("email")
        password = request.data.get("password")
        if not email or not password:
            return Response(data={"message": "Invalid username or password"},status = status.HTTP_401_UNAUTHORIZED)
        else:
            user = User.objects.get(email=email)
            if password == user.password:
                serializer = UserSerializer(user)
                return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
            return Response(data={"message":"Invalid username or passowrd"},status= status.HTTP_401_UNAUTHORIZED)
        

#logout
# Delete this function soon¸S
@csrf_exempt
def logout_user(request):
    pass
    