from django.shortcuts import render, redirect #import redirect
from django.contrib.auth import logout, login #import logout, login
from django.contrib.auth.forms import UserCreationForm #import wbudowanego formularza rejestracyjnego

# Create your views here.

#Utworzenie widoku wylogowania

def logout_view(request):
    logout(request)
    return redirect('learning_logs:index')

#Utworzenie widoku rejestracji użytkownika

def register(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST) #przekazanie danych formularza do klasy formularza tworzenia użytkownika

        if form.is_valid():
            new_user = form.save() #zapisanie w bazie nazwy użytkownika i hasła(hash)
            login(request, new_user) #autologowanie utworzonego użytkownika
            return redirect('learning_logs:index') #przekierowanie użytkownika na stronę główną

    context = {'form': form}
    return render(request, 'users/register.html', context)        

