from django.shortcuts import render

# Create your views here.

#Utworzenie widoku dla strony głównej (/index.html)

def index(request):
    return render(request, 'learning_logs/index.html')

   