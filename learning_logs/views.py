from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required #import potrzebny to ograniczenia dostępu tylko dla zalogowanych
from .models import Topic, Entry #importowanie modelu Topic oraz Entry
from .forms import TopicForm, EntryForm #importowanie modelu formularza dla new_topic, new_entry
from django.http import Http404 #import strony do obsługi błędu

#Utworzenie funkcji sprawdzającej czy użytkownik próbujący dostac się do tematu jest jego właścicielem

def check_topic_owner(request, topic): #przekazanie parametru request i topic
    if topic.owner != request.user: #sprawdzenie czy temat należy do zalogowanego użytkownika
        raise Http404 #jeżeli użytkownik nie jest ownerem otrzyma wyjątek ze stroną błędu 404

# Create your views here.

#Utworzenie widoku dla strony głównej (/index.html)

def index(request):
    return render(request, 'learning_logs/index.html')

#Utworzenie widoku dla tematów (/topics.html)

@login_required #Dostęp do widoku tylko po zalogowaniu
def topics(request):
    #topics = Topic.objects.order_by('date_added')  #Przypisanie obiektów (Tematów) z bazy danych przesortowanych po dacie chronologicznie
    topics = Topic.objects.filter(owner=request.user).order_by('date_added') #Przypisanie obiektów tematów z bazy, ale tylko powiązanych z użytkownikiem (twórcą) oraz sortowanie po dacie
    context = {'topics': topics} #context tworzymy w celu późniejszego wykorzystania kluczy w szablonach html
    return render(request, 'learning_logs/topics.html', context)

#Utworzenie widoku dla pojedynczego tematu (/topic/<id>.html)

@login_required #Dostęp do widoku tylko po zalogowaniu
def topic(request, topic_id): #topic_id przechwytuje <int:topic_id>
    topic = Topic.objects.get(id=topic_id) #funkcja get pobiera temat do topic_id przekazane zostaje id tematu
    check_topic_owner(request, topic)
    
    entries = topic.entry_set.order_by('-date_added') #Pobranie wpisów powiązanych z tematem z sortowaniem odwrotnym
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

#Utworzenie widoku tworzenia nowego tematu (/new_topic.html)

@login_required #Dostęp do widoku tylko po zalogowaniu
def new_topic(request):
    if request.method != 'POST': #jeżeli metoda żądania jest inna niż POST
        form = TopicForm() #To przekaż pusty formularz
    else:
        form = TopicForm(request.POST) #jeżeli metoda żądania to post
        if form.is_valid(): #sprawdzenie prawidłowości danych
            new_topic = form.save(commit=False) #zapisanie w danych w zmiennej
            new_topic.owner = request.user #przypisanie nazwy użytkownika do atrybutu owner
            new_topic.save() #zapisanie danych w bazie danych wraz z przypisanie tematu do nazwy ownera
            return redirect('learning_logs:topics')

    context = {'form': form} #przekazanie do contextu forma,aby wykorzystać go w new_topic.html 
    return render(request, 'learning_logs/new_topic.html', context) 

#Utworzenie widoku tworzenia nowego wpisu (/new_entry.html)

@login_required #Dostęp do widoku tylko po zalogowaniu
def new_entry(request, topic_id): #wykorzytanie topic_id dopasowanie wpisu do tematu
    topic = Topic.objects.get(id=topic_id) #funkcja get pobiera temat do topic_id przekazane zostaje id tematu
    check_topic_owner(request, topic)

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

#Utworzenie widoku edycji pojedynczego wpisu (/edit_entry<id>.html)

@login_required #Dostęp do widoku tylko po zalogowaniu
def edit_entry(request, entry_id): #wykorzytanie entry_id aby edytować wybrany wpis
    entry = Entry.objects.get(id=entry_id) #funkcja get pobiera entry do entry_id przekazane zostaje id wpisu
    topic = entry.topic #przypisuje temat pobrany z bazy dla tego wpisu
    check_topic_owner(request, topic)

    if request.method != 'POST':
        form = EntryForm(instance=entry) #argument instance=entry tworzy formularz wypełniony informacjami z obiektu istniejącego wpisu.
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id = topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)            


