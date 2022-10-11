from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from .forms import SignUpForm, EditProfileForm, PasswordChangingForm
# Create your views here.

'''
Django has premade form modules that can be imported.
At the top top of the page you will see

	from django.contrib.auth.forms

^^^^^^^^^^^^^^^^^
This is the module we are calling the forms from.

as class is initialised, just need to identify which class we want
to import.
	
	import UserCreationForm

^^^^^^^^^^^^^^^^^
is tagged on the end of the include module we are pulling on the end.
Further objects can be called again by delimitting with a comma and 
naming the form.

'''
class PasswordsChangeView(PasswordChangeView):
	form_class = PasswordChangingForm
	#from_class = PasswordChangeForm
	success_url = reverse_lazy('home')

class UserRegisterView(generic.CreateView):
	form_class = SignUpForm
	template_name = 'registration/register.html'
	success_url = reverse_lazy('login')
'''
class UserLoginView(generic.LoginView):
	form_class = UserLoginForm
	template_name = 'registration/login.html'
	success_url = 'home.html # a guestimate, actually sorted in settings
'''

class UserEditView(generic.UpdateView):
	#at the top of the page
	form_class = EditProfileForm
	template_name = 'registration/edit_profile.html'
	success_url = reverse_lazy('home')

	def get_object(self):
		return self.request.user
