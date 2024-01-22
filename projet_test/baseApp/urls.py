from django.contrib import admin
from django.urls import path, include
from baseApp.views import get_csrf_token

urlpatterns = [    
    path('token/',get_csrf_token,name='token'),  
]