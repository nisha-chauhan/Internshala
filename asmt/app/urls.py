from django.contrib import admin
from django.urls import path,include
from .views import *
from . import views
urlpatterns = [
    path('',default_page), 
    
    path('app/users/',users), 
    path('app/hello/',hello),
    path('app/add-user/',add_user),
    # path('app/user/<int:user_id>',each_user_detail),
    path('app/user/<int:user_id>/', each_user_detail),
    
    # path('app/delete-user/<int:user_id>/',delete_user),    
    # path('app/update-user/<int:user_id>',update_user),
    # path('app/do-update-user/<int:user_id>',do_update_user),
]