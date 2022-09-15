from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
from .forms import PostForm, EditForm

# Create your views here.
'''
def home(request):
	return render(request, 'home.html', {})
'''
class HomeView(ListView): # pass in ListView
	model = Post #so our post will appear as a list on homepage
	template_name = 'home.html' #home.html template already created

class ArticleDetailView(DetailView):
	model = Post
	template_name = 'article_detail.html'

class AddPostView(CreateView):
	model = Post
	form_class = PostForm
	template_name = 'add_post.html'
	#fields = '__all__'
	#fields = 'title', 'body'

class UpdatePostView(UpdateView):
	model = Post
	template_name = 'update_post.html'
	#fields = ['title', 'title_tag', 'body']
	form_class = EditForm