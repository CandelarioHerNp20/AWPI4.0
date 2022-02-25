from multiprocessing import context
import re
from django.shortcuts import render, redirect
from .models import Tarea
from .froms import TareaForm

# Create your views here.
def home(request):
    tareas = Tarea.objects.all()
    context = {'tareas': tareas}
    return render(request, 'vista/home.html', context)

def agregar(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form = TareaForm()
        
        context =('form': form)
        return  render(request, 'vista/agregar.html', context)