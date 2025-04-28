
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.utils import timezone
created_at = models.DateTimeField(default=timezone.now)

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='book_covers/', blank=True, null=True) 
    likes = models.ManyToManyField(User, related_name='liked_books', blank=True)
    
    def __str__(self):
        return self.title
    def total_likes(self):
            return self.likes.count()
    
class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Review by {self.reviewer} on {self.book.title}"

