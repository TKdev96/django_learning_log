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

#Utworzenie widoku dla pojedynczego tematu (/topic/<id>.html)

def topic(request, topic_id): #topic_id przechwytuje <int:topic_id>
    topic = Topic.objects.get(id=topic_id) #funkcja get pobiera temat do topic_id przekazane zostaje id tematu
    entries = topic.entry_set.order_by('-date_added') #Pobranie wpisów powiązanych z tematem z sortowaniem odwrotnym
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)