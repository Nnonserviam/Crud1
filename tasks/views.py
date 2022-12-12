from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import TaskForm
from .models import Task
from django.utils import timezone


# Create your views here.

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html',{
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tasks')
            except IntegrityError:
                return render(request, 'signup.html',{
                    'form': UserCreationForm,
                    "error": 'usuario ya existe'
                })
        return render(request, 'signup.html',{
            'form': UserCreationForm,
            "error": 'contraseñas no coinciden'
            })

def tasks(request):
    tasks = Task.objects.filter(usuario=request.user, fecha_completada__isnull=True)
    return render(request,'tasks.html', {'tasks': tasks})
def tasks_completed(request):
    tasks = Task.objects.filter(usuario=request.user, fecha_completada__isnull=False).order_by('-fecha_completada')
    return render(request,'tasks.html', {'tasks': tasks})
def create_task(request):
    if request.method == 'GET':
        return render(request, 'create_task.html',{
            'form': TaskForm
        })
    else:
        try:
            form = TaskForm(request.POST)
            nueva_tarea = form.save(commit=False)
            nueva_tarea.usuario = request.user
            nueva_tarea.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'create_task.html',{
                'form': TaskForm,
                'error': 'Provee datos validos'
            })

def task_detail(request,task_id):
    if request.method == 'GET':
        task = get_object_or_404(Task,pk=task_id,usuario=request.user)
        form= TaskForm(instance=task)
        return render(request,'task_detail.html',{'task':task,'form': form})
    else:
        try:
            task = get_object_or_404(Task, pk =task_id,usuario=request.user)
            form = TaskForm(request.POST, instance= task)
            form.save()
            return redirect('tasks')
        except ValueError:
            return render(request,'task_detail.html',{'task':task,'form': form,
            'error':'Error actualizando tarea'})

def complete_task(request,task_id):
    task = get_object_or_404(Task,pk=task_id,usuario = request.user)
    if request.method == 'POST':
        task.fecha_completada = timezone.now()
        task.save()
        return redirect('tasks')

def delete_task(request,task_id):
    task = get_object_or_404(Task,pk=task_id,usuario = request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')

def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html',{
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password= request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña incorrecta'
            })
        else:
            login(request, user)
            return redirect('tasks')
