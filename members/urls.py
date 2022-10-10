#initialise the django framework urls module
from django.urls import path
#from . import views
from .views import UserRegisterView, UserEditView
'''
Views.py is already inheriting from
   from django.contrib.auth.forms
^^^^^^^^^^^^^^^^^^^^
specific objects in those modules have already been pulled
   UserRegisterView, UserEditView
^^^^^^^^^^^^^^^^^^^^
   from django.contrib.auth.forms
no longer needs to referenced as it is much simpler to refer to
objects in .views
'''
urlpatterns = [
   path('register/', UserRegisterView.as_view(), name='register'),
   path('edit_profile/', UserRegisterView.as_view(), name='edit_profile'),
   #path('login/', UserLoginView.as_view(), name='register')

]
    