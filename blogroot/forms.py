from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import Post, Category, User, Comment
#from django.contrib.auth.models import User

#cats = [('coding','coding'),('sports','sports'),('entertainment','entertainment')]
cat = Category.objects.all().values_list('name','name')

cat_choice = []

for item in cat:
	cat_choice.append(item)

#usernames = User.objects.username().values_list('username','username')
 
#if username in usernames == User.username:
#	usernames.append(username)
class PostForm(forms.ModelForm):

		class Meta:
			model = Post
			fields = ('title', 'title_tag', 'author', 'category', 'body','snippet','header_image')

			def __init__(self, *args, **kwargs):
				# first call parent's constructor
				super(PostForm, self).__init__(*args, **kwargs)
				# there's a `fields` property now
				self.fields['author'].required = False
			
			

			#'author' : forms.CharField(required=False , widget=forms.TextInput(attrs={'readonly':'True'}))

			widgets = {
				'title': forms.TextInput(attrs={'class': 'form-control'}),
				'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
				#'author': forms.Select(attrs={'class': 'form-control'}), 
				'author': forms.TextInput(attrs={'class': 'form-control','value':'','id':'author_box','readonly' : True, 'type': 'hidden'}),
				'category': forms.Select(choices = cat_choice, attrs={'class': 'form-control'}),
				#'category': forms.Select(attrs={'class': 'form-control'}),
				'body': forms.Textarea(attrs={'class': 'form-control'}),
				'snippet':forms.Textarea(attrs={'class': 'form-control','placeholder':'blog preview, max 140 characters.'}),

			}
class EditForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'title_tag', 'body', 'category')

		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
			#'author': forms.Select(attrs={'class': 'form-control'}),
			'category': forms.Select(choices = cat_choice, attrs={'class': 'form-control'}),
			'body': forms.Textarea(attrs={'class': 'form-control'}),

		}

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

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('author','body')

		widgets = {
			'author': forms.TextInput(attrs={'class': 'form-control','value':'','id':'author_box','readonly' : True, 'type': 'hidden'}),
			'body': forms.Textarea(attrs={'class': 'form-control'}),

		}
		def __init__(self, *args, **kwargs):
				# first call parent's constructor
				super(CommentForm, self).__init__(*args, **kwargs)
				# there's a `fields` property now
				self.fields['author'].required = False