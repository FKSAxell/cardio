from django.db import models
from django.utils import timezone
import datetime
# Create your models here.


def genero():
    return [(1,"Mujer"),(2,"Hombre")]
def caracteristica():
    return [(1,"Normal"),(2,"Encima de Normal"),(3,"Muy por Encima de Normal")]
def sino():
    return [(0,"No"),(1,"Si")]

class Persona(models.Model):
    cedula = models.CharField(max_length=10,default="0")
    nombre = models.CharField(max_length=100,default="")
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    fecha_de_nacimiento = models.DateTimeField()
    genero = models.IntegerField(choices=genero(),default="Hombre")
    altura_en_cm = models.IntegerField(default=0) #default
    peso_en_kg=models.DecimalField(max_digits=3,decimal_places=1)#default
    presión_sanguínea_sistólica=models.IntegerField(default=0)#default
    presión_sanguínea_diastolica = models.IntegerField(default=0)  # default
    colesterol = models.IntegerField(choices=caracteristica(),default="Normal")
    glucosa = models.IntegerField(choices=caracteristica(),default="Normal")
    fuma = models.IntegerField(choices=sino(),default="No")
    consume_alcohol = models.IntegerField(choices=sino(),default="No")
    actividad_física= models.IntegerField(choices=sino(),default="No")
    porcentaje = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    sino=models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)

class consultaForm(models.Model):
    cedula = models.CharField(max_length=10)

class PersonaDB(models.Model):
    # Cedula
    # Nombre
    age=models.IntegerField()
    gender=models.IntegerField()
    height=models.IntegerField()
    weight=models.DecimalField(max_digits=3,decimal_places=1)
    ap_hi=models.IntegerField()
    ap_lo=models.IntegerField()
    cholesterol=models.IntegerField()
    gluc=models.IntegerField()
    smoke=models.IntegerField()
    alco=models.IntegerField()
    active=models.IntegerField()
    cardio=models.IntegerField()








