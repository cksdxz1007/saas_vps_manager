from django.shortcuts import render, redirect
from .models import Service
from .forms import ServiceForm

def index(request):
    services = Service.objects.all()
    return render(request, 'services/index.html', {'services': services})

def add_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ServiceForm()
    return render(request, 'services/add_service.html', {'form': form})
