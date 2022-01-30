from django.shortcuts import render, redirect

from .models import Topic #importowanie modelu Topic
from .forms import TopicForm #importowanie modelu formularza dla new_topic

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

#Utworzenie widoku tworzenia nowego tematu (/new_topic.html)

def new_topic(request):
    if request.method != 'POST': #jeżeli metoda żądania jest inna niż POST
        form = TopicForm() #To przekaż pusty formularz
    else:
        form = TopicForm(request.POST) #jeżeli metoda żądania to post
        if form.is_valid(): #sprawdzenie prawidłowości danych
            form.save() #zapisanie w bazie danych
            return redirect('learning_logs:topics')

    context = {'form': form} #przekazanie do contextu forma,aby wykorzystać go w new_topic.html 
    return render(request, 'learning_logs/new_topic.html', context)               