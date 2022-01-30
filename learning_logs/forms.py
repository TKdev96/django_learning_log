from django import forms  #import modułu wbudowanych formularzy

from .models import Topic #import modelu Topic

class TopicForm(forms.ModelForm): #Utworzenie klasy TopicForm z przekazanym modelem formularza
    class Meta:
        model = Topic #Budowanie formularza o model Topic
        fields = ['text'] #Możliwość wprowadzania tylko treść do pola text
        labels = {'text': ''} #informacja, że kolumna text nie ma etykiety
        

