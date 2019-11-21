from rest_framework import serializers
from toDoListBackEnd.todolist.models import  User, ToDoList, ToDoItem




# Serializer for the todo items
class ToDoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoItem
        fields = ['item_name','list_id','date_created']

# Serializer for the todo list itself
class ToDoListSerializer(serializers.ModelSerializer):
    # We include the ToDoItemSerializer in our list in order
    # to include the actual list items within our JSON list
    list_items = ToDoItemSerializer(many=True) 
    class Meta:
        model = ToDoList
        fields = ['list_name','user_id','list_items']

"""{list_id:1,
    list_name:'shopping list',
    list_items:[{
        item_name:'oranges',
        date_created: dt.now()
        },
        {item_name:'apples',
         date_created: dt.now()}
        ]}"""
class UserSerializer(serializers.ModelSerializer):
    todolists = ToDoListSerializer(many=True)
    class Meta:
        model = User
        fields = ['user_id','first_name','last_name','email','date_created','todolists']
