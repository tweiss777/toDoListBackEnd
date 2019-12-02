from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from . import views

urlpatterns = [
    path('retrievelistitems',views.retrieveToDoItems),# retrieve items for a particular to do list
    path('create_list',views.create_list),# create a new to do list for the user
    path('create_list_item',views.create_list_item),# create a new list item for a particular to do list
    path('update_list_item',views.update_list_item),# change the name of the item in a to do list
    path('update_list_name',views.update_list_name),# change the name of a to do list for the user
    path('delete_list',views.delete_list),# delete the list for that user 
    path('delete_list_item',views.delete_list_item),# delete list item from a particular list
    path('retrievelists',views.retrieveToDoLists),# retrieve the list of a user
    path('login',views.login_user),# login the user and show the all the list for the user
    path('create_account',views.create_account),# creates a new account
]