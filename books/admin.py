from django.contrib import admin
from django.contrib import admin
from .models import Book, Review, Genre

admin.site.register(Book)
admin.site.register(Review)
admin.site.register(Genre)

