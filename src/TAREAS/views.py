from django.shortcuts import render, redirect
from APPTareas.models import Task
from APPTareas.forms import FormTask

def inicio(request):
    tareas = Task.objects.all()
    form = FormTask()
    if request.method == 'POST':
        form = FormTask(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    contexto = {'tareas':tareas, 'form': form }
    return render(request,'index.html',contexto)

def editar_tarea(request, pk):
    
    tarea = Task.objects.get(id=pk)
    form = FormTask(instance = tarea)

    if request.method == 'POST':
        form = FormTask(request.POST, instance = tarea)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form }
    return render(request,'editar_tarea.html',context)

def borrar(request,pk):
    tarea = Task.objects.get(id=pk)
    if request.method == 'POST':
        tarea.delete()
        return redirect('/')

    context = {'tarea':tarea }
    return render(request,'borrar.html',context)

def delete_all(request):
    tarea = Task.objects.all()
    if request.method == 'POST':
        tarea.delete()
        return redirect('/')
    context = {'tarea':tarea}
    return render(request,'delete_all.html',context)