from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy


# Create your views here.
'''
def home(request):
	return render(request, 'home.html', {})
'''
class HomeView(ListView): # pass in ListView
	model = Post #so our post will appear as a list on homepage
	template_name = 'home.html' #home.html template already created
	#ordering = ['-id']
	ordering = ['-post_date']

	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(HomeView, self).get_context_data(*args, **kwargs)
		context["cat_menu"] = cat_menu
		return context

def CategoryListView(request):
	cat_menu_list = Category.objects.all()
	return render(request, 'category_list.html', {'cat_menu_list':cat_menu_list})

def CategoryView(request, cats):
	category_posts = Post.objects.filter(category=cats.replace('-',' '))
	return render(request, 'categories.html', {'cats':cats.replace('-',' '), 'category_posts':category_posts})

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

class DeletePostView(DeleteView):
	model = Post
	template_name = 'delete_post.html'
	success_url = reverse_lazy('home')

class AddCategoryView(CreateView):
	model = Category
	#form_class = PostForm
	template_name = 'add_category.html'
	fields = '__all__'
	#fields = 'title', 'body'