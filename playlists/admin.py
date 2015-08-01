from django.contrib import admin
from .models import Category, Playlist, Song


admin.site.register(Category)
admin.site.register(Playlist)
admin.site.register(Song)
