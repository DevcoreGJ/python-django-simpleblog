from django import forms
from .models import Post, Category, User

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
			def __init__(self, *args, **kwargs):
				# first call parent's constructor
				super(PostForm, self).__init__(*args, **kwargs)
				# there's a `fields` property now
				self.fields['author'].required = False
			model = Post
			fields = ('title', 'title_tag', 'author', 'category', 'body')

			#'author' : forms.CharField(required=False , widget=forms.TextInput(attrs={'readonly':'True'}))

			widgets = {
				'title': forms.TextInput(attrs={'class': 'form-control'}),
				'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
				#'author': forms.Select(attrs={'class': 'form-control'}), 
				'author': forms.TextInput(attrs={'class': 'form-control','value':'','id':'author_box','readonly' : True, 'type': 'hidden'}),
				'category': forms.Select(choices = cat_choice, attrs={'class': 'form-control'}),
				#'category': forms.Select(attrs={'class': 'form-control'}),
				'body': forms.Textarea(attrs={'class': 'form-control'}),


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