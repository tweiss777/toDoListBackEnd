from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('retrievelist',views.retrieveToDoItems),
    path('create_list',views.create_list),
    path('create_list_item',views.create_list_item),
    path('update_list_item',views.update_list_item),
    path('update_list_name',views.update_list_name),
    path('delete_list',views.delete_list),
    path('delete_list_item',views.delete_list_item),
    path('retrievelists',views.retrieveToDoLists),
    path('login',views.create_account),
    path('create_account',views.login)
]