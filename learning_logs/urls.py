from django.urls import path #import path

from . import views #import views

app_name = 'learning_logs' #Konieczne jest dodanie nazwy aplikacji

urlpatterns = [
    #Dodanie strony głównej
    path('', views.index, name='index'),
    #Dodanie widoku Tematów
    path('topics/', views.topics, name='topics'),
    #Dodanie widoków poszczególnych tematów
    path('topics/<int:topic_id>', views.topic, name="topic"),

]