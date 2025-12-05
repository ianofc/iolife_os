from django.shortcuts import render
from .models import Log

def flow_home(request):
    # Pega todos os logs (posts), ordenados por data
    logs = Log.objects.all() 
    return render(request, 'flow/home.html', {'logs': logs})