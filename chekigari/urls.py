from django.contrib import admin
from django.urls import path, include
from . import views

# app_name = "chekigari"
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('viewdata/', views.viewdata, name='viewdata'),
    path('insert', views.insert, name="insert"),
    path('contact/', views.contact, name='contact'),
    path('sendMessage', views.sendMessage, name='sendMessage'),
    path('delete/<id>', views.delete, name='delete'),
    path('viewmessages/', views.viewMessages, name='viewMessages'),
    path('deleteMessage/<id>', views.deleteMessage, name='deleteMessage'),
    path('edituser/<id>', views.edituser, name="edituser"),
    path('shop/', views.shop, name='shop')

]
