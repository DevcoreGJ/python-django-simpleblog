from django.contrib import admin

# Register your models here.
from .models import Post

admin.site.register(Post) # Posts are accessable in admin area