from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
import random

# Create your views here.
def create_appointment(request):
    if request.method == 'POST':
        validacion=validaciones()
        if (validacion==True):
            return HttpResponseRedirect(reverse('measurementCreate'))
        else:
            return HttpResponseRedirect(reverse('measurementNotCreated'))


def aleatorio():
    numero = random.uniform(0,1)
    return numero


def validaciones():
    #revisar que el paciente exista
    if aleatorio()>0.9:
        return False
    #revisar que el paciente no tenga una cita    
    if aleatorio()>0.95:
        return False
    #revisar que el doctor exista
    if aleatorio()>0.94:
        return False
    #revisar que el doctor no tenga una cita
    if aleatorio()>0.85:
        return False
    #revisar que la sala este disponible
    if aleatorio()>0.9:
        return False
    #revisar que la maquinaria este disponible
    if aleatorio()>0.96:
        return False
    else:
        return True


