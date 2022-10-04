from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
#added additional fields to register form
#email field
#first_name field
#last_name field
#to sign up form. Applied forms widget.
#applied bootstrap form-control html attribute.
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
	first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
#although these are now how I want them, manipulating
#fields unlisted here requires a method
#method is defined beneath meta*
#def __init__(self, *args, **kwargs):

	class Meta:
		model = User
		fields = ('username','first_name','last_name','email','password1','password2')

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['class'] = 'form-control'