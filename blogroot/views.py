from django.shortcuts import render
from django.views.generic import ListView, DetailView


# Create your views here.
'''
def home(request):
	return render(request, 'home.html', {})
'''
class HomeView(ListView): # pass in ListView
	model = Post #so our post will appear as a list on homepage
	template_name = ' home.html' #home html template already created