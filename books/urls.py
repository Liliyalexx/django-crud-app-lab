from django.urls import path
from . import views
from django.conf.urls.static import static
from .views import (
    Home,
    BookList, BookDetail, BookCreate, BookUpdate, BookDelete,
    ReviewCreateView, ReviewListView, ReviewDetailView,
    ReviewUpdateView, ReviewDeleteView, Home, 
    signup,
)
from django.contrib.auth import views as auth_views  


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    
    # Book URLs
    path('books/', BookList.as_view(), name='book_list'),
    path('book/<int:pk>/', BookDetail.as_view(), name='book_detail'),
    path('book/create/', BookCreate.as_view(), name='book_create'),
    path('book/<int:pk>/update/', BookUpdate.as_view(), name='book_update'),
    path('book/<int:pk>/delete/', BookDelete.as_view(), name='book_delete'),
   
    
    # Review URLs
    path('reviews/', ReviewListView.as_view(), name='review_list'),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review_detail'),
    path('reviews/create/', ReviewCreateView.as_view(), name='review_create'),
    path('reviews/<int:pk>/update/', ReviewUpdateView.as_view(), name='review_update'),
    path('reviews/<int:pk>/delete/', ReviewDeleteView.as_view(), name='review_delete'),
    path('book/<int:pk>/like/', views.toggle_like, name='book_like'),
    path('book/<int:pk>/review/', views.ReviewCreateView.as_view(), name='book_review'),
]