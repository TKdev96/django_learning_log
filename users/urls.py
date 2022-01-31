from django.contrib.auth.views import LoginView #importowanie wbudowanego widoku LoginView
from django.urls import path #importowanie urls path

app_name = 'users' #przypisanie nazwy aplikacji konieczne

urlpatterns = [
    path('login/', LoginView.as_view(template_name = 'users/login.html'), name='login'), #utworzenie ścieżki z użyciem klasy LoginView i przypisanie własnego szablonu html
]
