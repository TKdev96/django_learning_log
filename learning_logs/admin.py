from django.contrib import admin
from learning_logs.models import Topic, Entry #import modelu Topic z learning_logs.models later import Entry
# Register your models here.

admin.site.register(Topic) #Rejestracja obsługi modelu Topic
admin.site.register(Entry) #Rejestracja obsługi modelu Entry


