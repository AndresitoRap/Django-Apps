from django.forms import modelform_factory

from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.
from personas.models import Persona, Domicilio


def detallePersona(request, id):
    persona = Persona.objects.get(pk=id)
    return render(request, 'personas/detalle.html', {'persona': persona})


PersonaForm = modelform_factory(Persona, exclude=[])


def nuevaPersona(request):
    if request.method == 'POST':
        formaPersona = PersonaForm(request.POST)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('index')
    else:
        formaPersona = PersonaForm()
    return render(request, 'personas/nuevo.html', {'formaPersona': formaPersona})


def editarPersona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    if request.method == 'POST':
        formaPersona = PersonaForm(request.POST, instance=persona)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('index')
    else:

        formaPersona = PersonaForm(instance=persona)
    return render(request, 'personas/editar.html', {'formaPersona': formaPersona})


def eliminarpersona(request, id):
    persona = get_object_or_404(Persona, id=id)
    persona.delete()
    return redirect('index')


def detalleDomicilio(request, id):
    domicilio = Domicilio.objects.get(pk=id)
    return render(request, 'personas/detalle_domicilio.html', {'domicilio': domicilio})


DomicilioForm = modelform_factory(Domicilio, exclude=[])


def nuevoDomicilio(request):
    if request.method == 'POST':
        formaDomicilio = DomicilioForm(request.POST)
        if formaDomicilio.is_valid():
            formaDomicilio.save()
            return redirect('index')
    else:
        formaDomicilio = DomicilioForm()
    return render(request, 'personas/nuevo_domicilio.html', {'formaDomicilio': formaDomicilio})


def editarDomicilio(request, id):
    domicilio = get_object_or_404(Domicilio, pk=id)
    if request.method == 'POST':
        formaDomicilio = DomicilioForm(request.POST, instance=domicilio)
        if formaDomicilio.is_valid():
            formaDomicilio.save()
            return redirect('index')
    else:

        formaDomicilio = DomicilioForm(instance=domicilio)
    return render(request, 'personas/editar_domicilio.html', {'formaDomicilio': formaDomicilio})


def eliminarDomicilio(request, id):
    domicilio = get_object_or_404(Domicilio, id=id)
    domicilio.delete()
    return redirect('index')
