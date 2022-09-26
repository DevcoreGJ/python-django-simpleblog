from django.contrib import admin

# Register your models here.
from .models import Post, Category

admin.site.register(Post) # Posts are accessable in admin area
admin.site.register(Category) # Posts are accessable in admin area