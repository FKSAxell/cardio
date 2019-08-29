from django import forms

from .models import Persona
from .models import consultaForm

class DateInput(forms.DateInput):
    input_type = 'date'
class PersonaForm(forms.ModelForm):
    #Todos los datos son obligatorios indicar abajo de datos paciente
    class Meta:
        model = Persona

        fields = ('cedula','nombre','fecha_de_nacimiento','genero','genero', 'altura_en_cm','peso_en_kg','presión_sanguínea_diastolica','presión_sanguínea_sistólica','colesterol','glucosa','fuma','consume_alcohol','actividad_física')
        widgets = {
            'fecha_de_nacimiento': DateInput(),
        }

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = consultaForm
        fields = ('cedula',)


