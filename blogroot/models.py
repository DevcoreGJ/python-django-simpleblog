from django.db import models
from django.urls import reverse
from datetime import datetime, date

# Create your models here.
from django.contrib.auth.models import User

class Category(models.Model):
	name = models.CharField(max_length=255)
	def __str__(self):
		return self.name
	def get_absolute_url(self):
		#return reverse('article_detail', args=(str(self.id)) )
		return reverse('home')

class Post(models.Model):
	title = models.CharField(max_length=255) #max char length
	title_tag = models.CharField(max_length=255)
	#author = models.CharField(max_length=50)
	#author = models.ForeignKey(User, on_delete=models.NULL) #if user is deleted all related posts are
	author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
	body = models.TextField() #input field for text
	name = "Apollo Blog"
	post_date = models.DateField(auto_now_add = True)
	category = models.CharField(max_length=255, default='development')
	likes = models.ManyToManyField(User, related_name='blog_posts')
	
	def total_likes(self):
		return self.likes.count()

	def __str__(self):
		return self.title + ' | ' + str(self.author)

	def get_absolute_url(self):
		#return reverse('article_detail', args=(str(self.id)) )
		return reverse('home')

	
