from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Book, Review
from .forms import ReviewForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST


class Home(LoginView):
    template_name = 'home.html'

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('book_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def about(request):
    contact_details = 'you can reach support at suport@bookcollector.com'
    return render(request, 'about.html', {
        'contact': contact_details
    })


# views.py
def book_index(request):
  books = Book.objects.all() 
  return render(request, 'books/index.html', {'books': books})

# views.py

def book_detail(request, pk):  # Change parameter to pk
    book = Book.objects.get(id=pk)
    return render(request, 'books/detail.html', {
        'book': book,  
    })
@login_required
@require_POST
def toggle_like(request, pk):
    book = get_object_or_404(Book, pk=pk)
    liked = False
    if request.user in book.likes.all():
        book.likes.remove(request.user)
    else:
        book.likes.add(request.user)
        liked = True
    return JsonResponse({
        'liked': liked,
        'likes_count': book.likes.count(),
    })

@login_required
def add_review(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.reviewer = request.user
            review.save()
            return JsonResponse({
                'username': request.user.username,
                'text': review.text,
            })
    return JsonResponse({'error': 'Invalid form'}, status=400)

class BookList(ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'object_list'

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')

        book_id = request.POST.get('book_id')
        content = request.POST.get('review')
        book = get_object_or_404(Book, pk=book_id)

        if content:
            Review.objects.create(book=book, reviewer=request.user, content=content)

        return redirect('book_list')


class BookDetail(DetailView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = '/books'

class BookCreate(LoginRequiredMixin, CreateView):
    model = Book
    fields = ['title', 'author', 'description', 'image']  
    success_url = reverse_lazy('book_list')
    login_url = '/login/'

class BookUpdate(LoginRequiredMixin, UpdateView):
    model = Book
    fields = ['title', 'author', 'description', 'image'] 
    template_name = 'books/book_form.html'
    success_url = reverse_lazy('book_list')

class BookDelete(LoginRequiredMixin, DeleteView):
    model = Book
    success_url = reverse_lazy('book_list')
    
class ReviewCreateView(CreateView):
    model = Review
    fields = ['book', 'reviewer', 'content']
    template_name = 'reviews/review_form.html'

class ReviewListView(ListView):
    model = Review

class ReviewDetailView(DetailView):
    model = Review

class ReviewUpdateView(UpdateView):
    model = Review
    fields = ['reviewer', 'content']
    success_url = '/'

class ReviewDeleteView(DeleteView):
    model = Review
    success_url = '/'