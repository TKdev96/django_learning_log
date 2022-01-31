from django.shortcuts import render, redirect #import redirect
from django.contrib.auth import logout

# Create your views here.

#Utworzenie funkcji wylogowania
def logout_view(request):
    logout(request)
    return redirect('learning_logs:index')
