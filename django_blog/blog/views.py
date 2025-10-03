from django.shortcuts import render

# blog/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomUserCreationForm

# Create your views here.

# Registration View
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in user after registration
            return redirect('home')  # Redirect to home or wherever you want
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

# Login View (using built-in)
class CustomLoginView(LoginView):
    template_name = 'blog/login.html'

# Logout View (using built-in)
class CustomLogoutView(LogoutView):
    next_page = 'login'  # Redirect after logout