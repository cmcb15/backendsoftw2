from django.db import models

class Usuario_Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    usuario = models.CharField(max_length=50)
    password = models.CharField(max_length=10)

class Usuario_Guia(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    usuario = models.CharField(max_length=50)
    password = models.CharField(max_length=10) 
