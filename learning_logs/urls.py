from django.conf.urls import path #import path

from . import views #import views

urlpatterns = [
    #Dodanie strony głównej
    path('', views.index, name='index'),
]