from django import forms
from serialApp.models import Participante

class FormParticipante(forms.ModelForm):
    class Meta:
        model = Participante
        fields = ['id','nombre','telefono','fecha_inscripcion','institucion','hora_inscripcion','email','estado','observacion']
    
    def __init__(self, *args, **kwargs):
        super(FormParticipante, self).__init__(*args, **kwargs)
        self.fields['observacion'].required = False