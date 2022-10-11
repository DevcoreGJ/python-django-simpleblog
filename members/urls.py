#initialise the django framework urls module
from django.urls import path
#from . import views
from .views import UserRegisterView, UserEditView, PasswordChangeView
from django.contrib.auth import views as auth_views
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
   path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
   #path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html'))

#in reference to password change
#in views.py created a class caled PasswordsChangeView
#That class inherits the original PasswordChangeView class.
#It adds in a reverse lazy so it redirecte back home on success.
#where originallt it would go to a django success page.

   path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html')),
   #path('login/', UserLoginView.as_view(), name='register')

]
    