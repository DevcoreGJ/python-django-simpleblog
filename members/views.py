from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


#imported as class ShowProfilePageView inherits DetailView
from django.views.generic import DetailView, CreateView

#originally our change password name was using auth views module.
#This was rep;aced with a bespoke view class.
from django.contrib.auth.views import PasswordChangeView

from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm, PasswordChangingForm, ProfilePageForm
from blogroot.models import Profile



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

class CreateProfilePageView(CreateView): #This class is my view
	#When a View Class is created we need to tell it what model to used:
	model = Profile #This relates to my already created model.
	# It handles data for the view.
	
	form_class = ProfilePageForm

	#all members app templates reside in registration folder.
	#what webpage is it modifying? point it to the the HTML file. 
	template_name = "registration/create_user_profile_page.html" 
	#^^^^^ this refers to my URL.
	#Once made create the template file.
	#urls need to be registered in urls.py

	#fields = '__all__' replaced by profile page form

	#allows our project to figure out which user is filling out the form.
	#create a function.
	#if the form is valid pass in arguments from CreateProfilePageView.
	#Pass arguements from the form being referenced.
	def form_valid(self, form):
		#this specific form session calls current user credentials
		#get CreateProfilePageForm user object from this instance
		#overload by setting the user from Profile model 
		form.instance.user = self.request.user
		#Super allows method access to CreateProfilePageView.
		#returns from class form_valid, passing arguements from form
		return super().form_valid(form)


class EditProfilePageView(generic.UpdateView):
	model = Profile
	template_name = 'registration/edit_profile_page.html'
	fields = ['bio', 'profile_pic', 'website_url', 'FB_url', 'twitter_url', 'instagram_url','pinterest_url']
	success_url = reverse_lazy('home')

class ShowProfilePageView(DetailView):
	model = Profile
	template_name = 'registration/user_profile.html'

	def get_context_data(self, *args, **kwargs):
		cat_menu = Profile.objects.all()
		context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
		#self.kwargs gets primary key is getting passed in by the url.
		page_user = get_object_or_404(Profile, id=self.kwargs['pk'])

		context["page_user"] = page_user
		return context


class PasswordsChangeView(PasswordChangeView):
	#this new form doesn't have the weird bullet points.
	#They now appear as dynamic error messages if you make a mistake.
	#from_class = PasswordChangeForm
	form_class = PasswordChangingForm
	success_url = reverse_lazy('password_success')
	#success_url = reverse_lazy('home')
def password_success(request):
	return render(request, 'registration/password_success.html', {})

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
