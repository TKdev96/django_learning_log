from django.shortcuts import render

from .models import Topic #importowanie modelu Topic

# Create your views here.

#Utworzenie widoku dla strony głównej (/index.html)

def index(request):
    return render(request, 'learning_logs/index.html')

#Utworzenie widoku dla tematów (/topics.html)

def topics(request):
    topics = Topic.objects.order_by('date_added')  #Przypisanie obiektów (Tematów) z bazy danych przesortowanych po dacie chronologicznie
    context = {'topics': topics} #context tworzymy w celu późniejszego wykorzystania kluczy w szablonach html
    return render(request, 'learning_logs/topics.html', context)
      