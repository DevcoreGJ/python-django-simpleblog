from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Post, Category, User
from .forms import PostForm, EditForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

# Create your views here.
'''
def home(request):
	return render(request, 'home.html', {})
'''
def LikeView(request, pk):
	post = get_object_or_404(Post, id=request.POST.get('post_id'))
	liked = False
	#pass in a request to filter the id of a user that is logged in
	#look up if a like has been liked by user id and if it exists do something.
	#if liked by the auth'd user id exists, remove it.
	if post.likes.filter(id=request.user.id).exists():
		post.likes.remove(request.user)
		liked = False
	else: #if not liked add the like.
		post.likes.add(request.user)
		liked = True
	return HttpResponseRedirect(reverse('article_detail', args=[str(pk)]))

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
	category_posts = Post.objects.filter(category= cats.replace('-',' '))
	return render(request, 'categories.html', {'cats':cats.replace('-',' '), 'category_posts':category_posts})

class ArticleDetailView(DetailView):
	model = Post
	template_name = 'article_detail.html'
	
	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
		
		post_by_id = get_object_or_404(Post, id=self.kwargs['pk'])#Looks up article detail by id
		total_likes = post_by_id.total_likes()
		#likes default state is false
		#references itself instead of passing request argument
		#request id from user on the post id, check if a like exists
		#if not, likes specific post
		liked = False
		if post_by_id.likes.filter(id=self.request.user.id).exists():
			liked = True


		context["cat_menu"] = cat_menu
		context["total_likes"] = total_likes #how many likes to display on article_detail
		#pass llked variable in to context
		#now liked is passed to context it is possible to use on HTML page
		context["liked"] = liked
		return context

class AddPostView(CreateView):
	model = Post
	form_class = PostForm
	template_name = 'add_post.html'
	#fields = '__all__'
	#fields = 'title', 'body'
	'author' == User.username
	

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
	#fields = 'title', 'title_tag', 'body'