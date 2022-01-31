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
    #Dodanie widoku tworzenia nowego tematu przez użytkownika
    path('new_topic/', views.new_topic, name='new_topic'),
    #Dodanie widoku tworzenia nowego wpisu przez użytkownika
    path('new_entry/<int:topic_id>', views.new_entry, name='new_entry'),
    #Dodanie widoku edycji pojedynczego wpisu przez użytkownika
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),

]