from django.db import models
from django.urls import reverse
from datetime import datetime, date

# Create your models here.
from django.contrib.auth.models import User

class Post(models.Model):
	title = models.CharField(max_length=255) #max char length
	title_tag = models.CharField(max_length=255)
	author = models.ForeignKey(User, on_delete=models.CASCADE) #if user is deleted all related posts are
	body = models.TextField() #input field for text
	name = "Apollo Blog"
	post_date = models.DateField(auto_now_add = True)
	 #

	def __str__(self):
		return self.title + ' | ' + str(self.author)

	def get_absolute_url(self):
		#return reverse('article_detail', args=(str(self.id)) )
		return reverse('home')

	
