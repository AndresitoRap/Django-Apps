from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from personas.models import Persona, Domicilio


def bienvenido(request):
    no_personas_var = Persona.objects.count()
    no_domicilio_var = Domicilio.objects.count()
    personas = Persona.objects.order_by('id')
    domicilio = Domicilio.objects.order_by('id')
    return render(request, 'bienvenido.html',
                  {'no_personas': no_personas_var, 'personas': personas, 'no_domicilio': no_domicilio_var,
                   'domicilio': domicilio, })


def despedirse(request):
    return HttpResponse('hasta pronto')
