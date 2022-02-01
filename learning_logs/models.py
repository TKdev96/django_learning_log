from django.db import models
from django.contrib.auth.models import User #importowanie user, aby umożliwić powiązanie tematów z użytkownikiem który je utworzył 

# Create your models here.
# Page 503
class Topic(models.Model):
    """Topic displayed for users"""
    text = models.CharField(max_length=200) #pole text czyli nazwa tematu, Charfield określa max długość znaków
    date_added = models.DateTimeField(auto_now_add=True) #pole data określone po aktualnej dacie i godzinie dodania
    owner = models.ForeignKey(User, on_delete=models.CASCADE) #Dodanie w bazie kolumny owner do modelu Topic i powiązanie jej z użytkownikiem

    def __str__(self):
        """Zwraca tekstową reprezentację modelu"""
        return self.text

class Entry(models.Model):
    """Entry to the topic"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE) #ForeignKey pozwala przypisywać entry do Topic, page 508
    text = models.TextField() #pole tekstowe dla treści wpisu
    date_added = models.DateTimeField(auto_now_add=True) #data utworzenia wpisu

    class Meta: #Meta przechowuje informacje dodatkowe dla modelu Entry, użycie formy entries podczas odwoływania się do więcej niż tylko jednego wpisu.
        verbose_name_plural = 'entries'

    def __str__(self):
        """Zwraca tekstowa reprezentację modelu"""
        return  self.text[:50] + "..." #jeżeli string ma 50 znaków to go ucina i dodaje trzy kropki

