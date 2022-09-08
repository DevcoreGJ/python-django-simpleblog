from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Post(models.Model):
	title = models.CharField(max_length=255) #max char length
	author = models.ForeignKey(User, on_delete=models.CASCADE) #if user is deleted all related posts are
	body = models.TextField() #input field for text

	def __str__(self):
		return self.title + ' | ' + str(self.author)
