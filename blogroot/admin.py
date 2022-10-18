from django.contrib import admin

# Register your models here.
from .models import Post, Category, Profile, Comment

admin.site.register(Post) # Posts are accessable in admin area
admin.site.register(Category) # Posts are accessable in admin area
admin.site.register(Profile) # Let's the added profile class in Models show in
#djago admin area.

admin.site.register(Comment) # Comment section will show up in Django admin area.