from django.urls import path
from . import views

app_name = "chekigari"  # prevents namespace conflic. always include it
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.loginform, name='login'),
    path('register/', views.register, name='register'),
    path('viewdata/', views.viewdata, name='viewdata'),
    path('insert', views.insert, name="insert"),  # Performs the registration of new users
    path('contact/', views.contact, name='contact'),
    path('sendMessage', views.sendMessage, name='sendMessage'),
    path('delete/<id>', views.delete, name='delete'),
    path('viewmessages/', views.viewMessages, name='viewMessages'),
    path('deleteMessage/<id>', views.deleteMessage, name='deleteMessage'),
    path('edituser/<id>', views.edituser, name="edituser"),
    path('shopcars/', views.shop, name='shop'),
    path('signup/', views.signup, name='signup'),  # Renders the signup form
    path('signupdata', views.signupdata, name='signupdata'),  # performs the signup action
    path('userlogin', views.userlogin, name='userlogin'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('viewvehicle/', views.viewvehicle, name='viewvehicle'),
    path('cart/', views.cart, name='cart'),  # Renders the cart file
    path('uploads/', views.uploads, name='uploads'),
    path('addvehicle/', views.addvehicle, name='addvehicle'),
    path('addvehicletodb', views.addvehicletodb,  name='addvehicletodb'),
    path('uploadfiles', views.uploadfiles, name='uploadfiles')

]
