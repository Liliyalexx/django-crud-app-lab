# library/views.py
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login'))  # Redirect to login page
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
