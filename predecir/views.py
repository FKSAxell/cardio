from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required

from .forms import PersonaForm
from .forms import ConsultaForm
from sklearn.externals import joblib
import numpy as np
import datetime
from django.template import RequestContext
# Create your views here.
from predecir.models import Persona
from predecir.models import consultaForm
from django.db.models import Count
@login_required
def dashboardView(request):
    return render(request,'dashboard.html')

def persona_new(request):
    if request.method == "POST":
        form = PersonaForm(request.POST)
        if form.is_valid():
            persona = form.save(commit=False)
            persona.author = request.user
            classifier = joblib.load("modelo.sav")
            dias= int((datetime.date.today() - (persona.fecha_de_nacimiento).date()).total_seconds()//86400)
            #dias = 18393
            X_new = np.array([dias, persona.genero, persona.altura_en_cm, float(persona.peso_en_kg), persona.presión_sanguínea_sistólica,persona.presión_sanguínea_diastolica, persona.colesterol,
                              persona.glucosa, persona.fuma, persona.consume_alcohol, persona.actividad_física]).reshape(-1, 1).T
            new_prediction = classifier.predict(X_new)
            n = new_prediction[0]
            porcen = classifier.predict_proba(X_new)[0][1] * 100
            persona.porcentaje = porcen
            persona.sino=n
            persona.save()
            #consulta = Persona.objects.filter(cedula=persona.cedula)
            nombre = persona.nombre
            return render(request, "resultado.html",
                         {'n': n, 'porcentaje': round(porcen, 2),
                          'nombre': nombre})
    else:
        form = PersonaForm()
    return render(request, 'persona.html',{'form': form})

def consulta(request):
    if (request.method =="POST"):
        form= ConsultaForm(request.POST)
        cedulaF=form.save(commit=False)
        consulta = Persona.objects.filter(cedula=cedulaF.cedula)
        return render(request, 'consultaCedula.html', {'consulta':consulta})

    else:
        sino= Persona.objects.values('sino').annotate(num=Count('sino'))
        form = ConsultaForm()
        return render(request, 'consulta.html', {'form': form ,'sino':sino})
