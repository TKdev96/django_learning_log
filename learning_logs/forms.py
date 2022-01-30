from django import forms  #import modułu wbudowanych formularzy

from .models import Topic, Entry #import modelu Topic

class TopicForm(forms.ModelForm): #Utworzenie klasy TopicForm z przekazanym modelem formularza
    class Meta:
        model = Topic #Budowanie formularza o model Topic
        fields = ['text'] #Możliwość wprowadzania tylko treść do pola text
        labels = {'text': ''} #informacja, że kolumna text nie ma etykiety


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})} #Nadpisanie ustawień aby dla kolumny 'text' wyświetlic textarea o szerokości 80

