from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth, messages
from django.contrib.auth import authenticate, login

# Create your views here.
def home(request):
    return render(request,'home.html')
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'home.html', {'form': form})
def loginuser(request):
 
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
 
        if user is not None:
            auth.login(request, user)
            return redirect('home')
 
        else:
            messages.error(request, 'Error wrong username/password')
            redirect('login')
 
    return render(request, 'login.html')
def logoutuser(request):
    auth.logout(request)
    return redirect('login')

