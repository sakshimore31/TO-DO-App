from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from .models import Mytodo
from .forms import TodoForm
from .forms import RegisterForm
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            auth_login(request,user)
            return redirect('login')  
    else:
        form = RegisterForm()  
    
    return render(request, 'registration.html', {'form': form})  

def login(request):
    if request.method=='POST':
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username= form.cleaned_data.get('username')
            password= form.cleaned_data.get('password')
            user= authenticate(username=username, password=password)
            if user is not None:
                auth_login(request,user)
                return redirect('alltodos')
    else:
        form= AuthenticationForm()
    return render(request, 'login.html', {'form':form})
    

@login_required
def alltodos(request):
    tasks = Mytodo.objects.all()
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'alltodo.html', {'tasks': tasks, 'form': form})

def deleteItem(request, pk):
    task = Mytodo.objects.get(id = pk)
    task.delete()
    return redirect('alltodos')

def updateItem(request, pk):
    todo = Mytodo.objects.get(id=pk)
    updateForm = TodoForm(instance = todo)
    if request.method == 'POST':
        updateForm = TodoForm(request.POST, instance = todo)
        if updateForm.is_valid():
            updateForm.save()
            return redirect('alltodos')
    return render(request, 'updateItem.html', {'todo':todo, 'updateform': updateForm})


# def home(request):
#     return render(request, 'home.html')

