from django.shortcuts import render, redirect

from .models import Topic #importowanie modelu Topic
from .forms import TopicForm, EntryForm #importowanie modelu formularza dla new_topic, new_entry

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

#Utworzenie widoku tworzenia nowego wpisu (/new_entry.html)

def new_entry(request, topic_id): #wykorzytanie topic_id dopasowanie wpisu do tematu
    topic = Topic.objects.get(id=topic_id) #funkcja get pobiera temat do topic_id przekazane zostaje id tematu

    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST) #przetwarzanie danych z formularza
        if form.is_valid():
            new_entry = form.save(commit=False) #commit=False nakazuje utworzenie nowego obiektu wpisu, i przechowanie w zmiennej new_entry - Bez zapisania w bazie danych
            new_entry.topic = topic #Przypisanie tematu pobranego z bazy danych
            new_entry.save() #zapisanie w bazie danych wpisu z przypisanym mu tematem
            return redirect('learning_logs:topic', topic_id = topic_id) #przekierowanie użytkownika na stronę tematu, przekazujemy id tematu

    context = {'topic': topic, 'form': form} #przekazanie do contextu forma i tematu,aby wykorzystać je w new_entry.html
    return render(request, 'learning_logs/new_entry.html', context)
