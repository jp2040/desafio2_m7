from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse
from .models import Estudiante, Profesor, Curso

def crear_curso(request):
    return HttpResponse("Curso creado")

def crear_profesor(request):
    return HttpResponse("Profesor creado")

# Implementa las otras funciones de vista de manera similar


