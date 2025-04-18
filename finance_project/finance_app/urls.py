from django.contrib import admin
from django.urls import path,include
from finance_app.views import * 

urlpatterns = [
   path('',home_view,name="home"),
]