from django.shortcuts import render
from django.http import HttpResponse
import random
from .models import Project


def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects':projects})

def about(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/about.html', {'projects':projects})

def generator(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/generator.html', {'projects':projects})

def password(request):
    
    
    characters = list('abcdefghijklmnopqrstuvwxyz')
    
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRTSUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('+!%/=()&@'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
    
    length = int(request.GET.get('length' ,12))
    
    thepassword = ''
    
    for x in range(length):
        thepassword += random.choice(characters)
    
    return render(request, 'portfolio/password.html' , {'password':thepassword})

