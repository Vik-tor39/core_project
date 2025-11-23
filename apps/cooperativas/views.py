from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):

    if request.method == 'POST':
        form = CooperativaForm(request.POST)

        if form.is_valid():
            form.save()            
            messages.success(request, 'Cooperativa registrada con éxito')
            return redirect('index')

        else:
            messages.error(request, 'Algo salió mal, no se pudo registrar la cooperativa.')

    else:
        form = CooperativaForm()

    return render(request, 'cooperativas/index.html', {'form': form})