from django.contrib import admin
from .models import Note
# Register your models here.
admin.site.register(Note)


"""
create a posts app
 - create the app
 - register the app on settings
 - crete a urls.py in the posts
 - register the post.urls in config.urls
"""