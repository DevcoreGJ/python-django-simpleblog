from django.contrib import admin

# Register your models here.
from .models import Post, Category, Profile

admin.site.register(Post) # Posts are accessable in admin area
admin.site.register(Category) # Posts are accessable in admin area
admin.site.register(Profile) # Let's the added profile class in Models show in
#djago admin area.