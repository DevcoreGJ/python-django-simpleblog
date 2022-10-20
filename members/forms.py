from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from blogroot.models import Profile

class ProfilePageForm(forms.ModelForm):
	class Meta:

		model = Profile
		fields = ('bio','profile_pic','website_url','FB_url','twitter_url','instagram_url','pinterest_url')

		widgets = {
			'bio' : forms.Textarea(attrs={'class':'form-control'}),
			#'profile_pic' : forms.TextInput(attrs={'class':'form-control'}),
			'website_url' : forms.TextInput(attrs={'class':'form-control'}),
			'FB_url' : forms.TextInput(attrs={'class':'form-control'}),
			'twitter_url' : forms.TextInput(attrs={'class':'form-control'}),
			'instagram_url' : forms.TextInput(attrs={'class':'form-control'}),
			'pinterest_url' : forms.TextInput(attrs={'class':'form-control'}),

		}

class SignUpForm(UserCreationForm):
#added additional fields to register form
#email field
#first_name field
#last_name field
#to sign up form. Applied forms widget.
#applied bootstrap form-control html attribute.
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control','type':'EmailField'}))
	first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control','type':'CharField'}))
	last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control','type':'CharField'}))
#although these are now how I want them, manipulating
#fields unlisted here requires a method
#method is defined beneath meta*
#def __init__(self, *args, **kwargs):

	class Meta:
		model = User
		fields = ('username','first_name','last_name','email','password1','password2')

	def __init__(self, *args, **kwargs):
#super returns super object within a method as a proxy for the class.
#passing SignUpForm, and itself.
#initialise *args passing through any number number of positional arguements.
#**kwargs which takes any number of keyword arguements.
#in both instances args and kwargs are both standard naming conventions, * & ** respectively
#are what is the important part.
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['class'] = 'form-control'

'''
class UserChangeForm(UserCreationForm):
	class Meta:
		model = User
		fields = ('last_login','username','first_name','last_name','email',)

		def __init__(self, *args, **kwargs):
#super returns super object within a method as a proxy for the class.
#passing UserChangeForm, and itself.
#initialise *args passing through any number number of positional arguements.
#**kwargs which takes any number of keyword arguements.
#in both instances args and kwargs are both standard naming conventions, * & ** respectively
#are what is the important part.
		super(UserChangeForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['first_name'].widget.attrs['class'] = 'form-control'
		self.fields['last_name'].widget.attrs['class'] = 'form-control'
		self.fields['email'].widget.attrs['class'] = 'form-control'
		'''
class EditProfileForm(UserChangeForm):

	email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
	first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
	last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
	username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
	is_staff = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class':'form-check'}))
	last_login = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
	is_superuser = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class':'form-check'}))
	is_active = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class':'form-check'}))
	date_joined = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'is_superuser','is_active','date_joined',)
class PasswordChangingForm(PasswordChangeForm):
	old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
	new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
	new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

	class Meta:
		model = User
		fields = ('username','old_password','new_password1')

