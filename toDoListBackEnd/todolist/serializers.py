from rest_framework import serializers
from toDoListBackEnd.todolist.models import  User, ToDoList, ToDoItem

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id','first_name','last_name','email','password','date_created']



class ToDoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoItem
        fields = ['item_name','list_id','date_created']

class ToDoListSerializer(serializers.ModelSerializer):
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