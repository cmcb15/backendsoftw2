from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Usuario_Cliente, Usuario_Guia

# /endpoints/loginCliente
@csrf_exempt
def loginCliente(request):
    if request.method == "POST":
        dictDataRequest = json.loads(request.body)
        usuario = dictDataRequest["usuario"]
        password = dictDataRequest["password"]

        usuarios = Usuario_Cliente.objects.all()

        for u in usuarios: 
            if u.usuario == usuario and u.password == password:
                dictOK = {
                    'error': '',
                    'userid': u.pk
                }
                return HttpResponse(json.dumps(dictOK))
            else:
                dictError = {
                'error': 'No existe esa cuenta'
                }
                strError = json.dumps(dictError)
                return HttpResponse(strError)
    else:
        dictError = {
            'error': 'Tipo de peticion no existe'
        }
        strError = json.dumps(dictError)
        return HttpResponse(strError)
    
# /endpoints/loginGuia
@csrf_exempt
def loginGuia(request):
    if request.method == "POST":
        dictDataRequest = json.loads(request.body)
        usuario = dictDataRequest["usuario"]
        password = dictDataRequest["password"]

        usuarios = Usuario_Guia.objects.all()

        for u in usuarios: 
            if u.usuario == usuario and u.password == password:
                dictOK = {
                    'error': '',
                    'userid': u.pk
                }
                return HttpResponse(json.dumps(dictOK))
            else:
                dictError = {
                'error': 'No existe esa cuenta'
                }
                strError = json.dumps(dictError)
                return HttpResponse(strError)
    else:
        dictError = {
            'error': 'Tipo de peticion no existe'
        }
        strError = json.dumps(dictError)
        return HttpResponse(strError)

@csrf_exempt
def registrarCliente(request):
    if request.method != "POST":
        dictError = {
            "error": "Tipo de peticion no existe"
        }
        strError = json.dumps(dictError)
        return HttpResponse(strError)

    dictCliente = json.loads(request.body)
    nombre = dictCliente["nombre"]
    apellido = dictCliente["apellido"]
    usuario = dictCliente["usuario"]
    password = dictCliente["password"]

    cat = Usuario_Cliente(nombre=nombre, apellido=apellido, usuario=usuario, password=password)
    cat.save() # Registra en la bd la nueva categoria

    dictOK = {
        "error" : ""
    }
    return HttpResponse(json.dumps(dictOK))

@csrf_exempt
def registrarGuia(request):
    if request.method != "POST":
        dictError = {
            "error": "Tipo de peticion no existe"
        }
        strError = json.dumps(dictError)
        return HttpResponse(strError)

    dictGuia = json.loads(request.body)
    nombre = dictGuia["nombre"]
    apellido = dictGuia["apellido"]
    usuario = dictGuia["usuario"]
    password = dictGuia["password"]

    cat = Usuario_Guia(nombre=nombre, apellido=apellido, usuario=usuario, password=password)
    cat.save() # Registra en la bd la nueva categoria

    dictOK = {
        "error" : ""
    }
    return HttpResponse(json.dumps(dictOK))