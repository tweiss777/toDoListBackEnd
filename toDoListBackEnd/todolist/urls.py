from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from . import views

urlpatterns = [
    path('retrievelist',views.retrieveToDoItems),
    path('create_list',views.create_list),
    path('create_list_item',views.create_list_item),
    path('update_list_item',views.update_list_item),
    path('update_list_name',views.update_list_name),
    path('delete_list',views.delete_list),
    path('delete_list_item',views.delete_list_item),
    path('retrievelists',views.retrieveToDoLists),
    path('login',views.login_user),
    path('create_account',views.create_account),
]